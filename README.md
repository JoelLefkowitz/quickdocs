# Quickdocs

Creates HTML docs from a project's readme and sphinx-apidoc

## Status

| Source  | Shields                                                        |
| ------- | -------------------------------------------------------------- |
| Project | ![license][license] ![release][release]                        |
| Raised  | [![issues][issues]][issues_link] [![pulls][pulls]][pulls_link] |

## Installing

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
version: 1.0.0
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
readme_name:   # Default: "README.md"
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

Please view our [documentation][documentation] available on readthedocs.

To build locally generate the sphinx configuration:

```bash
quickdocs .quickdocs.yml
```

Then build the documentation:

```bash
sphinx-build -E docs build
```

## Changelog

Please read [CHANGELOG.md](CHANGELOG.md) for details on changes that have been made.

## Versioning

[SemVer][semver] is used for versioning. For a list of versions available, see the tags on this repository.

Bump2version is used to version and tag changes.
For example:

```bash
bump2version patch
```

Releases are made on every minor change.

## Author

-   **Joel Lefkowitz** - _Initial work_ - [Joel Lefkowitz][author]

See also the list of contributors who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## Acknowledgments

None yet!

[license]: https://img.shields.io/github/license/joellefkowitz/quickdocs
[release]: https://img.shields.io/github/v/tag/joellefkowitz/quickdocs
[issues]: https://img.shields.io/github/issues/joellefkowitz/quickdocs "Issues"
[pulls]: https://img.shields.io/github/issues-pr/joellefkowitz/quickdocs "Pull requests"
[pulls_link]: https://github.com/JoelLefkowitz/quickdocs/pulls
[issues_link]: https://github.com/JoelLefkowitz/quickdocs/issues
[documentation]: https://joellefkowitz-quickdocs.readthedocs.io/en/latest/
[author]: https://github.com/JoelLefkowitz
[semver]: http://semver.org/
