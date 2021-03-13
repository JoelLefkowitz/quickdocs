from quickdocs.state.inputs import Inputs
from quickdocs.state.paths import Paths


def test_paths() -> None:
    """
    Test Path state class.
    """
    paths = Paths(template_path="", template_dir="", output_dir="")
    assert paths.dct != {}


def test_inputs() -> None:
    """
    Test Inputs state class.
    """
    inputs = Inputs(project="", version="", author="", html_title="", github_url="")
    assert inputs.dct != {}
