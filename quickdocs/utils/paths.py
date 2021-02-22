import os
from pathlib import Path


def path_head(path: str) -> str:
    return os.path.split(path)[1]


def path_tail(path: str) -> str:
    return os.path.split(path)[0]


def path_base(path: str) -> str:
    return os.path.normpath(path).split(os.sep)[0]


def path_ext(path: str) -> str:
    return os.path.splitext(path)[1]


def replace_ext(path: str, ext: str) -> str:
    return path.replace(os.path.splitext(path)[1], ext)


def create_parents(path: str) -> None:
    Path(path_tail(path)).mkdir(parents=True, exist_ok=True)
