import warnings
from typing import List


def redundant_inputs(inputs: List[str]) -> None:
    warnings.warn(f"Redundant inputs: {inputs}")

    