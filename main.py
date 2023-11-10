import configparser
import os
import re
import subprocess
from pathlib import Path
from typing import Optional
import requests
from packaging.version import Version

DEFAULT_PATTERN = r'(?i)^(__version__|VERSION) *= *([\'"])v?(?P<version>.+?)\2'


def get_path_to_configuration_file():
    version_path = Path(get_env('INPUT_CONFIG_FILE_PATH')[0])
    if version_path.is_file():
        return version_path
    else:
        raise RuntimeError(f'"{version_path}" is not a file')


def read_config_file(config_file_path: Path) -> str:
    configs = configparser.ConfigParser()
    configs.read(config_file_path)
    return configs


def get_last_tag() -> Optional[Version]:
    headers = {
        "Authorization": f"Bearer {os.getenv('INPUT_REPO_TOKEN')}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    url = f"https://api.github.com/repos/{os.getenv('GITHUB_REPOSITORY')}/tags"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        tags = response.json()
        if tags:

            sorted_list = sorted(tags, key=lambda x: x['name'])

            last_tag = sorted_list[-1]['name']
            last_tag = re.sub('^v', '', last_tag.lower())
            print(f"Last version: {last_tag}")
            return Version(last_tag)
        else:
            return None

    else:
        print(f"Request failed with status code {response.status_code}")




def check_environment_version():
    # env_tag = get_env_version()
    # config_file_path = get_path_to_configuration_file()
    # config_file = read_config_file(config_file_path)
    # semvar_level = config_file['SEMVER']['level']
    semvar_level = os.getenv('SEMVER_LEVEL')
    env_tag = get_last_tag()

    new_version = get_new_version(env_tag, semvar_level)

    print(f"::set-output name=next_version::{str(new_version)}")


def get_new_version(version: Optional[Version], semvar_level: str) -> Version:
    """
    Increment the version according to the semvar level

    :param version: the version
    :param semvar_level: the semvar level
    :return: the incremented version
    """
    if version is None:
        print("No tags found")
        if semvar_level == 'major':
            return Version('1.0.0')
        elif semvar_level == 'minor':
            return Version('0.1.0')
        elif semvar_level == 'patch':
            return Version('0.0.1')
    new_version = ""
    if semvar_level == 'major':
        new_version = f"{version.major + 1}.{0}.{0}"
    elif semvar_level == 'minor':
        new_version = f"{version.major}.{version.minor + 1}.{0}"
    elif semvar_level == 'patch':
        new_version = f"{version.major}.{version.minor}.{version.micro + 1}"
        print(f"New version: {new_version}")
    return Version(new_version)


def main():
    check_environment_version()


def get_env_version() -> Optional[Version]:
    """
    Get the version from the environment variable GITHUB_REF

    :return: the version`
    """

    github_ref, github_ref_env_var = get_env('GITHUB_REF')
    tag_str = re.sub('^refs/tags/', '', github_ref.lower())
    try:
        tag = Version(tag_str)
    except ValueError as e:
        raise RuntimeError(f'{github_ref_env_var}, {e}')
    print(f'{github_ref_env_var} environment variable version: "{github_ref}"')
    return tag


def get_env(*names: str) -> tuple[str, str]:
    for name in names:
        value = os.getenv(name)
        if value:
            return value, name


if __name__ == '__main__':
    main()
