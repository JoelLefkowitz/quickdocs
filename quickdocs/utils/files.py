import os
import json
from typing import Callable, Dict

import yaml


def path_head(path: str) -> str:
    return os.path.splitext(path)[1]


def path_tail(path: str) -> str:
    return os.path.splitext(path)[0]


def path_base(path: str) -> str:
    return os.path.normpath(path).split(os.sep)[0]


def change_ext(path: str, ext: str) -> str:
    ext = ext if ext[0] == "." else "." + ext
    return path.replace(os.path.splitext(path)[1], ext)


def parse_json(path: str) -> Dict:
    with open(path, "r") as stream:
        return json.loads(stream.read())


def parse_yaml(path: str) -> Dict:
    with open(path, "r") as stream:
        return yaml.safe_load(stream)
