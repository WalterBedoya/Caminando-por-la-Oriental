class NoSacolError(Exception):
    def __init__(self, message="No tienes tarritos de sacol para oler"):
        self.message = message
        super().__init__(self.message)
