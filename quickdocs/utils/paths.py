import os
from pathlib import Path


def path_head(path: str) -> str:
    """
    Get the head of a path string.

    >>> path_head('/dir1/dir2/path.ext')
    'path.ext'

    Args:
        path (str): Path string.

    Returns:
        str: Path string's head.
    """
    return os.path.split(path)[1]


def path_tail(path: str) -> str:
    """
    Get the tail of a path string.

    >>> path_tail('/dir1/dir2/path.ext')
    '/dir1/dir2'

    Args:
        path (str): Path string.

    Returns:
        str: Path string's tail.
    """
    return os.path.split(path)[0]


def path_base(path: str) -> str:
    """
    Get the base of a path string.

    >>> path_base('/dir1/dir2/path.ext')
    ''

    >>> path_base('dir1/dir2/path.ext')
    'dir1'

    Args:
        path (str): Path string.

    Returns:
        str: Path string's base.
    """

    return os.path.normpath(path).split(os.sep)[0]


def path_ext(path: str) -> str:
    """
    Get the extension of a path string.

    >>> path_ext('/dir1/dir2/path.ext')
    '.ext'

    Args:
        path (str): Path string.

    Returns:
        str: Path string's extension.
    """
    return os.path.splitext(path)[1]


def replace_ext(path: str, ext: str) -> str:
    """
    Replace a path's extension with another.

    >>> replace_ext('/dir1/dir2/path.ext', '.ext2')
    '/dir1/dir2/path.ext2'

    Args:
        path (str): Path string.
        ext (str): New extension.

    Returns:
        str: Path string with new extension.
    """
    return path.replace(os.path.splitext(path)[1], ext)


def create_parents(path: str) -> None:
    """
    Create a path's parent directories.

    Args:
        path (str): Path string.
    """
    Path(path_tail(path)).mkdir(parents=True, exist_ok=True)


def reverse_to_root(project_root: str, output_dir: str) -> str:
    """

    Get the relative path required to move to a project's root from some output
    directory.

    >>> reverse_to_root('/dir1/dir2', '/dir1/dir3')
    '../dir2'

    Args:
        project_root (str): Root path string.
        output_dir (str): Directory path string.

    Returns:
        str: Path string.
    """
    return os.path.relpath(
        project_root,
        os.path.realpath(output_dir),
    )
