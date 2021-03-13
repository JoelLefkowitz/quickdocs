import os
import shutil
from argparse import ArgumentParser

from walkmate import get_child_files

from .state.inputs import Inputs
from .state.paths import Paths
from .utils.dicts import merge_dicts
from .utils.jinja import parse_template
from .utils.paths import (
    create_parents,
    path_head,
    replace_ext,
    reverse_to_root,
)

templates_dir = os.path.normpath(
    os.path.join(__file__, "..", "templates")
)

cli = ArgumentParser("Quickdocs")
cli.add_argument("input", help="Input file path")
cli.add_argument(
    "--output-dir",
    help="Output directory",
    default=os.path.join(os.getcwd(), "docs"),
)


def main() -> None:
    """
    Entrypoint for Quickdocs.
    Collects user input and generates templates.
    """
    args = cli.parse_args()
    inputs = Inputs.from_file(args.input)

    for template_path in get_child_files(templates_dir):
        paths = Paths(template_path, templates_dir, args.output_dir)

        render_context = merge_dicts(
            inputs.dct,
            paths.dct,
            {
                "reverse_to_root": reverse_to_root(
                    inputs.project_root, args.output_dir
                )
            },
        )

        create_parents(paths.output_path)

        if (
            paths.first_subdir == "static"
            or path_head(template_path) == "requirements.txt"
        ):
            shutil.copy(paths.template_path, paths.output_path)

        elif path_head(template_path) == "conf.j2":
            parse_template(
                paths.template_path,
                replace_ext(paths.output_path, ".py"),
                render_context,
            )

        else:
            parse_template(
                paths.template_path,
                replace_ext(paths.output_path, ".rst"),
                render_context,
            )


if __name__ == "__main__":
    main()
