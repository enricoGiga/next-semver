# Hello world docker action

The versioning of this action follows the [semantic versioning](https://semver.org/) specification.
This first version allows only `<major>.<minor>.<micro>` versioning.
Future versions will allow pre-release and post-release versions.
## What is semantic versioning?
`<major>.<minor>.<micro>`
* Major — increasing the major version usually breaks compatibility, allowing developers to remove the deprecated API or rework the existing ones. Users know about it and do not expect a smooth update.
* Minor — version increment implies adding new functionality without breaking compatibility.
* Micro — also known as bugfix version that includes fixing security vulnerabilities, etc.
## Inputs

# Get New Tag Version Action

This GitHub Action checks the last tag version released on GitHub and retrieves the next version to be released based on the specified version bump level in the configuration file.

## Inputs

### `repo_token`

**Required** The GitHub token to use for authentication.

### `config_file_path`

**Required** Path to the configuration file containing the level of the version to be bumped.
Example of configuration file if we want to increase the micro version:
![configfile.png](images%2Fconfigfile.png)
```yaml

```yaml
## Outputs

### `next_version`

The next version to be released based on the specified version bump level in the configuration file.

## Example Usage

```yaml
uses: enricoGiga/next-semvar@v1.0.0
with:
  repo_token: ${{ secrets.GITHUB_TOKEN }}
  config_file_path: './path/to/config/file.cfg'

