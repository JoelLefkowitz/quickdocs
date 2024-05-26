import io
import json
import pytest
import ruamel.yaml
from src.exceptions.files import UnrecognizedFormat
from src.exceptions.inputs import MissingInputs
from src.state.inputs import Inputs
from typing import Dict
from unittest.mock import mock_open, patch


def test_inputs_from_file(minimal_inputs: Dict[str, str]) -> None:
    """
    Test creation of Inputs instance from a file.
    """
    read_data = json.dumps(minimal_inputs)

    with patch("builtins.open", mock_open(None, read_data)):
        Inputs.from_file("inputs.json")

    buffer = io.BytesIO()
    yaml = ruamel.yaml.YAML()
    yaml.dump(minimal_inputs, buffer)
    read_data = buffer.getvalue().decode("utf-8")

    with patch("builtins.open", mock_open(None, read_data)):
        Inputs.from_file("inputs.yml")

    with patch("builtins.open", mock_open()):
        with pytest.raises(UnrecognizedFormat):
            Inputs.from_file("inputs.xyz")


def test_inputs_constraints(minimal_inputs: Dict[str, str]) -> None:
    """
    Test Inputs state class properties.
    """
    missing_inputs = minimal_inputs.copy()
    missing_inputs.pop("project")
    read_data = json.dumps(missing_inputs)

    with patch("builtins.open", mock_open(None, read_data)):
        with pytest.raises(MissingInputs):
            Inputs.from_file("inputs.json")

    redundant_inputs = minimal_inputs.copy()
    redundant_inputs["spirit_animal"] = "Shark"
    read_data = json.dumps(redundant_inputs)

    with patch("builtins.open", mock_open(None, read_data)):
        with pytest.warns(UserWarning):
            Inputs.from_file("inputs.json")


@pytest.fixture
def minimal_inputs() -> Dict[str, str]:
    """
    Minimal Inputs state class fixture.

    Returns:
        Dict[str, str]: Minimal inputs.
    """
    return {
        "project": "",
        "version": "",
        "author": "",
        "html_title": "",
        "github_url": "",
    }
