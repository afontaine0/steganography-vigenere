class UnsupportedCharacterException(Exception):
    def __init__(self, character: str):
        self.message = f"Character \"{character}\" is not supported"
        super().__init__(self.message)
