from setuptools import setup

if __name__ == "__main__":
    setup(
        install_requires=[
            "pypandoc",
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
                "pytest",
                "pytest-cov",
                "pytest-html",
                "pytest-sugar",
                "pytest-bdd",
                "pytest-watch",
            ],
        },
    )
