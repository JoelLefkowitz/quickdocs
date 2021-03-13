import os
from dataclasses import dataclass
from typing import Any, Mapping

from quickdocs.utils.paths import path_base


@dataclass
class Paths:
    template_path: str
    template_dir: str
    output_dir: str

    @property
    def dct(self) -> Mapping[str, Any]:
        """
        Dictionary representation of this instance.

        Returns:
            Dict: Dictionary representation.
        """
        return self.__dict__

    @property
    def local_path(self) -> str:
        """
        Relative path of this instance from the template directory.

        Returns:
            str: Relative path.
        """
        return os.path.relpath(self.template_path, self.template_dir)

    @property
    def output_path(self) -> str:
        """
        Relative path of this instance's output path.

        Returns:
            str: Relative path.
        """
        return os.path.join(self.output_dir, self.local_path)

    @property
    def first_subdir(self) -> str:
        """
        Base path of this instance's path from the template directory.

        Returns:
            str: Base path.
        """
        return path_base(self.local_path)
