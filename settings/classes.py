class Paths:
    def __init__(self):
        self.settings = None
        self.input = None
        self.output = None
        self.edited = None

class Settings:
    def __init__(self) -> None:
        self.paths: Paths = None
        self.mode = None
