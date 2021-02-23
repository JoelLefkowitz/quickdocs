import os
from typing import Any, Dict

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from .paths import path_head, path_tail


def parse_template(
    template_path: str,
    output_path: str,
    context: Dict[str, Any],
) -> None:
    env = Environment(
        loader=FileSystemLoader(
            path_tail(template_path), encoding="utf-8"
        ),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
        undefined=StrictUndefined,
    )

    env.filters["path_join"] = lambda paths: os.path.join(*paths)

    with open(output_path, "w") as stream:
        stream.write(
            env.get_template(path_head(template_path)).render(
                **context
            )
        )
