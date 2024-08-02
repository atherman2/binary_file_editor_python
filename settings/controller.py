from settings.get import get_core_path
from settings.get import get_attributes
from settings.classes import Paths
from settings.classes import Settings

def get_settings():
    paths = Paths()
    get_core_path(paths)
    settings = Settings()
    settings.paths = paths
    get_attributes(settings)
    return settings