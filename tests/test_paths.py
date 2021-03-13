from quickdocs.state.paths import Paths


def test_paths_properties() -> None:
    """
    Test Paths state class properties.
    """
    paths = Paths(
        template_path="templates/dir/template.j2",
        template_dir="templates",
        output_dir="output",
    )
    assert paths.local_path == "dir/template.j2"
    assert paths.output_path == "output/dir/template.j2"
    assert paths.first_subdir == "dir"
