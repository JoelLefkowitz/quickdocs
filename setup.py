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
            "dist": ["wheel", "twine", "bump2version"],
            "tests": [
                "tox",
                "pytest",
                "pytest-cov",
                "pytest-html",
                "pytest-sugar",
                "pytest-bdd",
                "pytest-watch",
            ],
        },
    )
