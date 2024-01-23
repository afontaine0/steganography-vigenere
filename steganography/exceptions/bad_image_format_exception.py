class BadImageFormatException(Exception):
    def __init__(self, expected_format: str, file: str):
        self.message = f"Bad format for \"{file}\". Expected \"{expected_format}\"."
        super().__init__(self.message)
