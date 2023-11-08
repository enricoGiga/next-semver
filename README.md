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

## `who-to-greet`

**Required** The name of the person to greet. Default `"World"`.

## Outputs

## `time`

The time we greeted you.

## Example usage

uses: actions/hello-world-docker-action@v2
with:
  who-to-greet: 'Mona the Octocat'

## How release a new version
git tag -a -m "My first action release" v1
git push --follow-tags
