from settings.get import get_core_path
from settings.get import get_attributes

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
    get_core_path(paths)
    settings = Settings()
    settings.paths = paths
    get_attributes(settings)