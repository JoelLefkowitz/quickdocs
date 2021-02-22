import warnings
from typing import List


class MissingInputs(Exception):
    def __init__(self, inputs: List[str]) -> None:
        super().__init__(f"Missing inputs: {inputs}")


def warn_redundant_inputs(inputs: List[str]) -> None:
    warnings.warn(f"Redundant inputs: {inputs}")
