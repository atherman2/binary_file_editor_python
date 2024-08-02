from settings.controller import Paths
from settings.controller import Settings

def get_core_path(paths_obj: Paths):
    paths_obj.settings = "./settings/settings.txt"

def get_attributes(settings_obj: Settings):
    with open(settings_obj.paths.settings, "rt") as settings_file:
        settings_list = []
        while(setting := settings_file.readline()):
            settings_list.append(setting)
        for setting in settings_list:
            settings_obj.paths.input = get_key_value_from_string(setting, "input")
            settings_obj.paths.output = get_key_value_from_string(setting, "output")
            settings_obj.paths.edited = get_key_value_from_string(setting, "edited")

def get_key_value_from_string(string, key):
    if string[:len(key)] == key:
        return string[(len(key)+1):]
    else:
        return None