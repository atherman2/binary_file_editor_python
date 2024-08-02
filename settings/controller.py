from settings.get import get_core_path

class Paths:
    def __init__(self):
        self.settings = None
        self.input = None
        self.output = None
        self.edited = None

class Settings:
    def __init__(self) -> None:
        self.paths = None
        self.mode = None

def get_settings():
    paths = Paths()
    paths.settings = get_core_path()