import json
from typing import Dict

import yaml


def parse_json(path: str) -> Dict:
    """
    Parse a json file.

    Args:
        path (str): Json file path.

    Returns:
        Dict: Dictionary of parsed data.
    """
    with open(path, "r") as stream:
        return json.load(stream)


def parse_yaml(path: str) -> Dict:
    """
    Parse a yaml file.

    Args:
        path (str): Yaml file path.

    Returns:
        Dict: Dictionary of parsed data.
    """
    with open(path, "r") as stream:
        return yaml.safe_load(stream)
