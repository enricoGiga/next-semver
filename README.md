# Get New Tag Version Action

This GitHub Action checks the last tag version released on GitHub and 
retrieves the next version to be released based on the specified 
version defined inside the environment variable **SEMVER_LEVEL**.
The versioning of this action follows the [semantic versioning](https://semver.org/) specification. 

- Format allowed to create tags: `v<major>.<minor>.<patch>`
- Regex: `^v?(\d+)\.(\d+)\.(\d+)$`
- Examples: v1.0.0, 0.1.0, v0.0.1, etc

## What is semantic versioning?
`v<major>.<minor>.<patch>`
* **Major** — increasing the major version usually breaks compatibility, allowing developers to remove the deprecated API or rework the existing ones. Users know about it and do not expect a smooth update.
* **Minor** — version increment implies adding new functionality without breaking compatibility.
* **patch** — also known as bugfix version that includes fixing security vulnerabilities, etc.

## Inputs

### `repo_token`

**Required** The GitHub token to use for authentication.



## Outputs

### `next_version`

The next version you should release based on the latest version uploaded to GitHub. 

For example, if the last version released is on GitHub is 2.4.5 it will give you the following outputs:

| SEMVER_LEVEL | LAST_VERSION | NEXT_VERSION |
|--------------|--------------|--------------|
| major        | 2.4.5        | 3.0.0        |
| minor        | 2.4.5        | 2.5.0        |
| patch        | 2.4.5        | 2.4.6        |

If there is no previous version it will return the first version based on the specified version defined inside the environment variable **SEMVER_LEVEL**:

| SEMVER_LEVEL | LAST_VERSION | NEXT_VERSION |
|--------------|--------------|--------------|
| major        | -            | 1.0.0        |
| minor        | -            | 0.1.0        |
| patch        | -            | 0.0.1        |

## env
**SEMVER_LEVEL** - The level of the version to be upgrade.
The possible values are: `major | minor | patch`

## Example Usage

```yaml
uses: enricoGiga/next-semvar@v1.0.1
env:
  SEMVER_LEVEL: patch
with:
  repo_token: ${{ secrets.GITHUB_TOKEN }}
```