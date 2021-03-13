# Quickdocs

Creates HTML docs from a project's readme and sphinx-apidoc.

## Status

| Source     | Shields                                                                                                                         |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Project    | ![release][release_shield] ![license][license_shield]  ![lines][lines_shield] ![languages][languages_shield]                    |
| Health     | ![codacy][codacy_shield] ![readthedocs][readthedocs_shield] ![travis][travis_shield] ![codacy_coverage][codacy_coverage_shield] |
| Repository | ![issues][issues_shield] ![issues_closed][issues_closed_shield] ![pulls][pulls_shield] ![pulls_closed][pulls_closed_shield]     |
| Publishers | ![pypi][pypi_shield] ![python_versions][python_versions_shield] ![pypi_downloads][pypi_downloads_shield]                        |
| Activity   | ![contributors][contributors_shield] ![monthly_commits][monthly_commits_shield] ![last_commit][last_commit_shield]              |

## Installation

```bash
pip install quickdocs
```

## Usage

To create an up to date sphinx configuration:

```bash
quickdocs .quickdocs.yml
```

Now we can build the documentation:

```bash
sphinx-build -E docs build
```

This will run copy and markup the project's readme at runtime so that you don't need to recompile the sphinx configuration unless any of the settings change.

Required settings file fields:

```yml
project: Quickdocs
version: 1.2.1
author: Joel Lefkowitz
html_title: Quickdocs
github_url: JoelLefkowitz/quickdocs
```

Optional settings:

```yml
debug: # Default: False
project_root: # Default: os.getcwd()
verbose_name: # Default: None
```

```yml
markup_readme: # Default: True
readme_path: # Default: "README.md"
```

```yml
apidoc_module_dir: # Default: None
```

### Integrating with readthedocs

**`.readthedocs.yml`**:

```yml
version: 2

sphinx:
  configuration: docs/conf.py

formats: all

python:
  version: 3.8
  install:
    - requirements: docs/requirements.txt
```

### Removing old documentation

The sphinx-apidoc plugin generates documentation under docs/api. When running, the sphinx plugin will overwrite but not delete out of date files in this directory. This means if you rename a module you must delete the out of date documentation. This package should not delete the docs/api directory because some developers will add custom documentation to this directory as they write new modules.

## Tests

To run unit tests and generate a coverage report:

```bash
grunt tests:unit
```

## Documentation

This repository's documentation is hosted on [readthedocs][readthedocs].

To generate the sphinx configuration:

```bash
grunt docs:generate
```

Then build the documentation:

```bash
grunt docs:build
```

## Tooling

To run linters:

```bash
grunt lint
```

To run formatters:

```bash
grunt format
```

Before committing new code:

```bash
grunt precommit
```

This will run linters, formatters, tests, generate a test coverage report and the sphinx configuration.

## Continuous integration

This repository uses Travis CI to build and test each commit. Formatting tasks and writing documentation must be done before committing new code.

## Versioning

This repository adheres to semantic versioning standards.
For more information on semantic versioning visit [SemVer][semver].

Bump2version is used to version and tag changes.
For example:

```bash
bump2version patch
```

## Changelog

Please read this repository's [CHANGELOG](CHANGELOG.md) for details on changes that have been made.

## Contributing

Please read this repository's guidelines on [CONTRIBUTING](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## Contributors

- **Joel Lefkowitz** - _Initial work_ - [Joel Lefkowitz][joellefkowitz]

[![Buy Me A Coffee][coffee_button]][coffee]

## Remarks

Lots of love to the open source community!

![Be kind][be_kind]

<!-- External links -->

[readthedocs]: https://joellefkowitz-quickdocs.readthedocs.io/en/latest/
[semver]: http://semver.org/
[coffee]: https://www.buymeacoffee.com/joellefkowitz
[coffee_button]: https://cdn.buymeacoffee.com/buttons/default-blue.png
[be_kind]: https://media.giphy.com/media/osAcIGTSyeovPq6Xph/giphy.gif

<!-- Acknowledgments -->

[joellefkowitz]: https://github.com/JoelLefkowitz

<!-- Project shields -->

[release_shield]: https://img.shields.io/github/v/tag/joellefkowitz/quickdocs
[license_shield]: https://img.shields.io/github/license/joellefkowitz/quickdocs
[lines_shield]: https://img.shields.io/tokei/lines/github/joellefkowitz/quickdocs
[languages_shield]: https://img.shields.io/github/languages/count/joellefkowitz/quickdocs

<!-- Health shields -->

[codacy_shield]: https://img.shields.io/codacy/grade/d2067acdcb594c47b8a63d5291c6612c
[readthedocs_shield]: https://img.shields.io/readthedocs/joellefkowitz-quickdocs
[travis_shield]: https://img.shields.io/travis/com/joellefkowitz/quickdocs
[codacy_coverage_shield]: https://img.shields.io/codacy/coverage/d2067acdcb594c47b8a63d5291c6612c

<!-- Repository shields -->

[issues_shield]: https://img.shields.io/github/issues/joellefkowitz/quickdocs
[issues_closed_shield]: https://img.shields.io/github/issues-closed/joellefkowitz/quickdocs
[pulls_shield]: https://img.shields.io/github/issues-pr/joellefkowitz/quickdocs
[pulls_closed_shield]: https://img.shields.io/github/issues-pr-closed/joellefkowitz/quickdocs

<!-- Publishers shields -->

[pypi_shield]: https://img.shields.io/pypi/v/quickdocs
[python_versions_shield]: https://img.shields.io/pypi/pyversions/quickdocs
[pypi_downloads_shield]: https://img.shields.io/pypi/dw/quickdocs

<!-- Activity shields -->

[contributors_shield]: https://img.shields.io/github/contributors/joellefkowitz/quickdocs
[monthly_commits_shield]: https://img.shields.io/github/commit-activity/m/joellefkowitz/quickdocs
[last_commit_shield]: https://img.shields.io/github/last-commit/joellefkowitz/quickdocs
