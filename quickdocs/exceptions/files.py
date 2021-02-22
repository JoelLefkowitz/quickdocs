class UnrecognisedFormat(Exception):
    def __init__(self, fmt: str) -> None:
        super().__init__(f"Unrecognised format: {fmt}")
