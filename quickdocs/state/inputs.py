import os
from dataclasses import dataclass
from typing import Any, Mapping, Optional, Set, get_type_hints

from quickdocs.exceptions.files import UnrecognizedFormat
from quickdocs.exceptions.inputs import (
    MissingInputs,
    warn_redundant_inputs,
)
from quickdocs.utils.files import parse_json, parse_yaml
from quickdocs.utils.paths import path_ext
from quickdocs.utils.types import cls_defaults


@dataclass
class Inputs:
    project: str
    version: str
    author: str
    html_title: str
    github_url: str

    # Defaults for templating
    debug: bool = False
    project_root: str = os.getcwd()
    verbose_name: Optional[str] = None

    # Readme settings
    markup_readme: bool = True
    readme_path: str = "README.md"

    # Apidoc settings
    apidoc_module_dir: Optional[str] = None

    @classmethod
    def from_file(cls, path):  # type: (str) -> Inputs
        """
        Read inputs from a file.

        Args:
            path (str): File path.

        Raises:
            UnrecognizedFormat: File format not able to be parsed.
            MissingInputs: Required input parameters missing.

        Returns:
            Inputs: Input instance.
        """
        file_type = path_ext(path)

        if file_type == ".json":
            inputs = parse_json(path)

        elif file_type in [".yml", ".yaml"]:
            inputs = parse_yaml(path)

        else:
            raise UnrecognizedFormat(file_type)

        missing_inputs = cls.missing_inputs(set(inputs.keys()))

        if missing_inputs:
            raise MissingInputs(list(missing_inputs))

        redundant_inputs = cls.redundant_inputs(set(inputs.keys()))

        if redundant_inputs:
            warn_redundant_inputs(list(redundant_inputs))
            inputs = {
                k: v
                for k, v in inputs.items()
                if k in cls.allowed_inputs()
            }

        return cls(**inputs)

    @property
    def dct(self) -> Mapping[str, Any]:
        """
        Dictionary representation of this instance.

        Returns:
            Dict: Dictionary representation.
        """
        return self.__dict__

    @classmethod
    def allowed_inputs(cls) -> Set[str]:
        """
        Collect the set of allowed input parameters.

        Returns:
            Set[str]: Set of allowed input parameters.
        """
        return set(get_type_hints(cls).keys())

    @classmethod
    def missing_inputs(cls, inputs: Set[str]) -> Set[str]:
        """
        Evaluate which required parameters are missing.

        Returns:
            Set[str]: Set of missing input parameters.
        """
        return cls.allowed_inputs() - cls_defaults(cls) - inputs

    @classmethod
    def redundant_inputs(cls, inputs: Set[str]) -> Set[str]:
        """
        Evaluate which required parameters are redundant.

        Returns:
            Set[str]: Set of redundant input parameters.
        """
        return inputs - cls.allowed_inputs()
