import json
import yaml
from typing import Callable, Dict


def modify_file(path: str, callback: Callable[[str], str]) -> None:
    with open(path, "r") as stream:
        content = stream.read()

    with open(path, "w") as stream:
        stream.write(callback(content))


def markup(md_path: str, target_dir: str) -> None:
    output_path = os.path.basename(md_path).replace(".md", ".html")

    with open(md_path, "r") as stream:
        content = stream.read()

    with open(os.path.join(target_dir, output_path), "w") as stream:
        stream.write(pypandoc.convert(content, "html", format="md"))


def parse_json(path: str) -> Dict:
    with open(path, "r") as stream:
        return json.loads(stream.read())


def parse_yaml(path: str) -> Dict:
    with open(path, "r") as stream:
        return yaml.safe_load(stream)
            
