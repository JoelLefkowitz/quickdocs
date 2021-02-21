from typing import List


class UnrecognisedFormat(Exception):
    def __init__(self, fmt: str) -> None:
        super().__init__(f"Unrecognised format: {fmt}")


class MissingInputs(Exception):
    def __init__(self, inputs: List[str]) -> None:
        super().__init__(f"Missing inputs: {inputs}")
