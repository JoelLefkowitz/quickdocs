import json
from typing import Dict

import yaml


def parse_json(path: str) -> Dict:
    with open(path, "r") as stream:
        return json.loads(stream.read())


def parse_yaml(path: str) -> Dict:
    with open(path, "r") as stream:
        return yaml.safe_load(stream)
