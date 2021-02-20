from __future__ import annotations

from dataclasses import dataclass
from typing import get_type_hints, List
from .utils.files import parse_json, parse_yaml
from .exceptions import UnrecognisedFormat, MissingInputs
from .warnings import redundant_inputs

@dataclass
class Inputs:
    project: str
    version: str
    author: str
    html_title: str
    apidoc_module_dir: str
    github_url: str

    @classmethod
    def from_file(cls, path: str, fmt: str) -> Inputs:
        if fmt.lower() == "json":
            inputs = parse_json(path)
        elif fmt.lower() in ["yml", "yaml"]:
            inputs = parse_yaml(path)
        else:
            raise UnrecognisedFormat(fmt)

        missing_inputs = cls.missing_inputs(inputs)
        redundant_inputs = cls.redundant_inputs(inputs)

        if missing_inputs: 
            raise MissingInputs(missing_inputs)
        
        if redundant_inputs: 
            redundant_inputs(redundant_inputs)

        return cls(**inputs)

    @staticmethod
    def missing_inputs(inputs: List[string]) -> List[string]:
        return list(set(get_type_hints(Inputs).keys()) - set(inputs))

    @staticmethod
    def redundant_inputs(inputs: List[string]) -> List[string]:
        return list(set(inputs) - set(get_type_hints(Inputs).keys()))