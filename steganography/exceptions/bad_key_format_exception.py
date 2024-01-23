class BadKeyFormatException(Exception):
    def __init__(self):
        self.message = "Expect the key to be a list of numbers separated by a comma (\",\")."
        super().__init__(self.message)
