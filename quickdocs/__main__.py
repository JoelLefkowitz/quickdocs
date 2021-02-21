import os
import shutil
from pathlib import Path

from walkmate import get_child_files

from .files import change_ext
from .inputs import Inputs
from .jinja import parse_template


if __name__ == "__main__":
    paths = {
        output_dir = "./quickdocs/dist"
        template_dir = "./quickdocs/templates"
    }
    
    inputs = Inputs.from_file("tests/fixtures/inputs.json", "json")

    render_context = dict(**paths, **inputs.__dict__)

    for path in get_child_files(template_dir):

        # Path relative to template_dir
        local_path = os.path.relpath(path, template_dir)

        # First segment of path relative to template_dir
        local_path_base = os.path.normpath(local_path).split(os.sep)[0]

        # Destination
        output_path = os.path.join(output_dir, local_path)
        Path(os.path.split(output_path)[0]).mkdir(parents=True, exist_ok=True)

        if local_path_base == "static":
            shutil.copy(path, output_path)

        elif local_path_base == "rst":
            output_path = change_ext(output_path, "rst")
            parse_template(path, output_path, render_context)

        else:
            output_path = change_ext(output_path, "py")
            parse_template(path, output_path, render_context)
