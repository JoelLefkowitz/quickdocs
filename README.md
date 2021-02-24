# Quickdocs

Creates HTML docs from a project's readme and sphinx-apidoc

## Status

| Source     | Shields                                                                                                            |
| ---------- | ------------------------------------------------------------------------------------------------------------------ |
| Project    | ![release][release_shield] ![license][license_shield]  ![dependents][dependents_shield]                            |
| Health     | ![travis][travis_shield] ![codacy][codacy_shield] ![coverage][coverage_shield] ![readthedocs][readthedocs_shield]  |
| Repository | ![issues][issues_shield] ![pulls][pulls_shield]                                                                    |
| Publishers | ![pypi][pypi_shield] ![python_versions][python_versions_shield] ![pypi_downloads][pypi_downloads_shield]           |
| Activity   | ![contributors][contributors_shield] ![monthly_commits][monthly_commits_shield] ![last_commit][last_commit_shield] |

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

Settings input file:

**`.quickdocs.yml`**:

```yml
project: Quickdocs
version: 1.2.1
author: Joel Lefkowitz
html_title: Quickdocs
github_url: JoelLefkowitz/quickdocs
```

Optional settings:

```yml
debug:        # Default: False
project_root: # Default: os.getcwd()
verbose_name: # Default: None
```

```yml
markup_readme: # Default: True
readme_path:   # Default: "README.md"
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
      - method: pip
        path: .
        extra_requirements:
            - docs
```

Declare the sphinx dependencies:

**`setup.py`**:

```python
from setuptools import setup

if __name__ == "__main__":
    setup(
        extras_require={
            "docs": [
                "pypandoc",
                "sphinx",
                "sphinxcontrib.apidoc",
                "sphinxcontrib.pandoc_markdown",
                "sphinx-autodoc-annotation",
                "yummy_sphinx_theme",
            ],
        },
    )
```

## Tests

To run unit tests:

```bash
tox
```

## Documentation

Please view our [documentation][readthedocs] available on readthedocs.

To build locally generate the sphinx configuration:

```bash
quickdocs .quickdocs.yml
```

Then build the documentation:

```bash
sphinx-build -E docs build
```

## Tooling

We use grunt to run local tooling before committing code:

### Linting

```bash
grunt lint
```

### Formatting

```bash
grunt format
```

Documentation and coverage reports should be regenerated before commiting any new code.

## Changelog

Please read [CHANGELOG.md](CHANGELOG.md) for details on changes that have been made.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Versioning

[SemVer][semver] is used for versioning. For a list of versions available, see the tags on this repository.

Bump2version is used to version and tag changes.
For example:

```bash
bump2version patch
```

Releases are made on every minor change.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## Contributors

- **Joel Lefkowitz** - _Initial work_ - [Joel Lefkowitz][joellefkowitz]

[![Buy Me A Coffee](https://cdn.buymeacoffee.com/buttons/default-blue.png)][coffee]

<!-- Github links -->
[pulls]: https://github.com/JoelLefkowitz/quickdocs/pulls
[issues]: https://github.com/JoelLefkowitz/quickdocs/issues

<!-- External links -->
[pypi]: https://pypi.org/project/randutils
[readthedocs]: https://joellefkowitz-quickdocs.readthedocs.io/en/latest/
[semver]: http://semver.org/
[coffee]: https://www.buymeacoffee.com/joellefkowitz

<!-- Acknowledgments -->
[joellefkowitz]: https://github.com/JoelLefkowitz

<!-- Shields -->
[release_shield]: https://img.shields.io/github/v/tag/joellefkowitz/quickdocs
[license_shield]: https://img.shields.io/github/license/joellefkowitz/quickdocs
[dependents_shield]: https://img.shields.io/librariesio/dependent-repos/pypi/quickdocs
[travis_shield]: https://img.shields.io/travis/joellefkowitz/quickdocs
[codacy_shield]: https://img.shields.io/codacy/coverage/quickdocs
[coverage_shield]: https://img.shields.io/codacy/grade/quickdocs
[readthedocs_shield]: https://img.shields.io/readthedocs/joellefkowitz-quickdocs
[issues_shield]: https://img.shields.io/github/issues/joellefkowitz/quickdocs
[pulls_shield]: https://img.shields.io/github/issues-pr/joellefkowitz/quickdocs
[pypi_shield]: https://img.shields.io/pypi/v/randutils
[python_versions_shield]: https://img.shields.io/pypi/pyversions/quickdocs
[pypi_downloads_shield]: https://img.shields.io/pypi/dw/randutils
[contributors_shield]: https://img.shields.io/github/contributors/joellefkowitz/quickdocs
[monthly_commits_shield]: https://img.shields.io/github/commit-activity/m/joellefkowitz/quickdocs
[last_commit_shield]: https://img.shields.io/github/last-commit/joellefkowitz/quickdocs
