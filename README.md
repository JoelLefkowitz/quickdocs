# Quickdocs

Creates HTML docs from a project's readme and sphinx-apidoc.

![Review](https://img.shields.io/github/actions/workflow/status/JoelLefkowitz/quickdocs/review.yml)
![Version](https://img.shields.io/pypi/v/quickdocs)
![Downloads](https://img.shields.io/pypi/dw/quickdocs)
![Quality](https://img.shields.io/codacy/grade/d2067acdcb594c47b8a63d5291c6612c)
![Coverage](https://img.shields.io/codacy/coverage/d2067acdcb594c47b8a63d5291c6612c)

## Installation

```bash
pip install quickdocs
```

## Documentation

Documentation and more detailed examples are hosted on [Github Pages](https://joellefkowitz.github.io/quickdocs).

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

## Tooling

### Dependencies

To install dependencies:

```bash
yarn install
pip install .[all]
```

### Tests

To run tests:

```bash
thx test
```

### Documentation

To generate the documentation locally:

```bash
thx docs
```

### Linters

To run linters:

```bash
thx lint
```

### Formatters

To run formatters:

```bash
thx format
```

## Contributing

Please read this repository's [Code of Conduct](CODE_OF_CONDUCT.md) which outlines our collaboration standards and the [Changelog](CHANGELOG.md) for details on breaking changes that have been made.

This repository adheres to semantic versioning standards. For more information on semantic versioning visit [SemVer](https://semver.org).

Bump2version is used to version and tag changes. For example:

```bash
bump2version patch
```

### Contributors

- [Joel Lefkowitz](https://github.com/joellefkowitz) - Initial work

## Remarks

Lots of love to the open source community!

<div align='center'>
    <img width=200 height=200 src='https://media.giphy.com/media/osAcIGTSyeovPq6Xph/giphy.gif' alt='Be kind to your mind' />
    <img width=200 height=200 src='https://media.giphy.com/media/KEAAbQ5clGWJwuJuZB/giphy.gif' alt='Love each other' />
    <img width=200 height=200 src='https://media.giphy.com/media/WRWykrFkxJA6JJuTvc/giphy.gif' alt="It's ok to have a bad day" />
</div>
