from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Dict, Optional, Set, get_type_hints

from quickdocs.exceptions.files import UnrecognisedFormat
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
    readme_name: str = "README.md"

    # Apicdoc settings
    apidoc_module_dir: Optional[str] = None

    @classmethod
    def from_file(cls, path: str) -> Inputs:
        file_type = path_ext(path)

        if file_type == ".json":
            inputs = parse_json(path)

        elif file_type in [".yml", ".yaml"]:
            inputs = parse_yaml(path)

        else:
            raise UnrecognisedFormat(file_type)

        missing_inputs = cls.missing_inputs(set(inputs.keys()))
        if missing_inputs:
            raise MissingInputs(list(missing_inputs))

        redundant_inputs = cls.redundant_inputs(set(inputs.keys()))
        if redundant_inputs:
            warn_redundant_inputs(list(redundant_inputs))

        return cls(**inputs)

    @property
    def dct(self) -> Dict:
        return self.__dict__

    @classmethod
    def allowed_inputs(cls) -> Set[str]:
        return set(get_type_hints(cls).keys())

    @classmethod
    def missing_inputs(cls, inputs: Set[str]) -> Set[str]:
        return cls.allowed_inputs() - cls_defaults(cls) - inputs

    @classmethod
    def redundant_inputs(cls, inputs: Set[str]) -> Set[str]:
        return inputs - cls.allowed_inputs()
