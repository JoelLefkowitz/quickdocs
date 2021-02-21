from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, get_type_hints

from .exceptions import MissingInputs, UnrecognisedFormat
from .files import parse_json, parse_yaml


@dataclass
class Inputs:
    project: str
    version: str
    author: str

    html_title: str
    github_url: str

    debug: Optional[bool] = False
    verbose_project: Optional[str] = None
    apidoc_module_dir: Optional[str] = None

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
        required = [k for k, v in get_type_hints(Inputs).items() if v not in [Optional[str], Optional[bool]]]
        return list(set(required) - set(inputs))

    @staticmethod
    def redundant_inputs(inputs: List[string]) -> List[string]:
        specified = get_type_hints(Inputs).keys()
        return list(set(inputs) - set(specified))
