class NotBinaryTextException(Exception):
    def __init__(self, text: str):
        self.message = f"Message \"{text}\" contains other characters than 0 or 1"
        super().__init__(self.message)
