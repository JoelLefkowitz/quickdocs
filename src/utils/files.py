import json
import ruamel.yaml
from typing import Any, Dict


def parse_json(path: str) -> Dict[str, Any]:
    """
    Parse a json file.

    Args:
        path (str): Json file path.

    Returns:
        Dict: Dictionary of parsed data.
    """
    with open(path, "r", encoding="utf8") as stream:
        return json.load(stream)


def parse_yaml(path: str) -> Dict[str, Any]:
    """
    Parse a yaml file.

    Args:
        path (str): Yaml file path.

    Returns:
        Dict: Dictionary of parsed data.
    """
    with open(path, "r", encoding="utf8") as stream:
        return ruamel.yaml.safe_load(stream)
