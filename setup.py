from setuptools import setup

if __name__ == "__main__":
    setup(
        entry_points={
            "console_scripts": ["quickdocs = quickdocs.__main__:main"]
        },
        install_requires=[
            "pypandoc",
            "pyyaml",
            "walkmate",
            "simple_pipes",
            "sphinx",
            "pyimport",
            "pypandoc",
            "sphinxcontrib.apidoc",
            "sphinxcontrib.pandoc_markdown",
            "sphinx-autodoc-annotation",
            "yummy_sphinx_theme",
        ],
        extras_require={
            "tests": [
                "pytest-bdd",
                "pytest-cov",
                "pytest-html",
                "pytest-sugar",
                "pytest-watch",
                "pytest",
                "tox",
            ],
            "tools": [
                "autoflake",
                "bandit",
                "black",
                "bump2version",
                "isort",
                "mypy",
                "pylint",
                "quickdocs",
                "twine",
                "wheel",
            ],
        },
    )
