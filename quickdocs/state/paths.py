import os
from dataclasses import dataclass
from typing import Dict

from quickdocs.utils.paths import path_base


@dataclass
class Paths:
    template_path: str
    template_dir: str
    output_dir: str

    @property
    def dct(self) -> Dict:
        return self.__dict__

    @property
    def local_path(self) -> str:
        return os.path.relpath(self.template_path, self.template_dir)

    @property
    def output_path(self) -> str:
        return os.path.join(self.output_dir, self.local_path)

    @property
    def first_subdir(self) -> str:
        return path_base(self.local_path)
