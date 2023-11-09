# semantic versioning action to get the next version to be released

The versioning of this action follows the [semantic versioning](https://semver.org/) specification.

Regex: ^v?(\d+)\.(\d+)\.(\d+)$
Example: v1.0.0, 0.1.0, v0.0.1, etc
## What is semantic versioning?
`v<major>.<minor>.<micro>`
* Major — increasing the major version usually breaks compatibility, allowing developers to remove the deprecated API or rework the existing ones. Users know about it and do not expect a smooth update.
* Minor — version increment implies adding new functionality without breaking compatibility.
* Micro — also known as bugfix version that includes fixing security vulnerabilities, etc.
## Inputs

# Get New Tag Version Action

This GitHub Action checks the last tag version released on GitHub and 
retrieves the next version to be released based on the specified 
version defined inside the environment variable **SEMVER_LEVEL**.

## Inputs

### `repo_token`

**Required** The GitHub token to use for authentication.

### env
SEMVER_LEVEL - The level of the version to be upgrade.
The possible values are: **major, minor, micro**.

## Outputs

### `next_version`

The next version to be released based on the specified version  level in the configuration file.
Examples: 
- if the previous version is 1.0.0 and the level is micro, the next version will be 1.0.1.
- if the previous version is 1.0.0 and the level is minor, the next version will be 1.1.0.
- if the previous version is 1.2.23 and the level is major, the next version will be 2.0.0.

If there is no previous version, the next version depends on the level specified in the configuration file.
For example, if the level is micro, the first version will be 0.0.1.

## Example Usage

```yaml
uses: enricoGiga/next-semvar@v1.0.1
env:
  SEMVER_LEVEL: micro
with:
  repo_token: ${{ secrets.GITHUB_TOKEN }}
```