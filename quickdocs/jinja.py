import os
from typing import Any, Dict


def parse_template(template_path: str, output_path: str, context: Dict[str, Any]):
    head, tail = os.path.split(template_path)

    env = Environment(
        loader=FileSystemLoader(tail, encoding="utf-8"),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
        undefined=StrictUndefined,
    )

    template = env.get_template(head)
    with open(output_path, "w") as stream:
        stream.write(template.render(context))
