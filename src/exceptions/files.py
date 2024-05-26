class UnrecognizedFormat(Exception):
    def __init__(self, fmt: str) -> None:
        super().__init__(f"Unrecognized format: {fmt}")
