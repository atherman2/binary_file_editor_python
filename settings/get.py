from settings.controller import Paths

def get_core_path():
    return "./settings/settings.txt"

def get_paths(core_path: str, paths_obj: Paths):
    with open(core_path, "rt") as settings_file:
        settings_list = []
        while(setting := settings_file.readline()):
            settings_list.append(setting)
        for setting in settings_list:
            Paths.input = get_key_value_from_string(setting, "input")
            Paths.output = get_key_value_from_string(setting, "output")
            Paths.edited = get_key_value_from_string(setting, "edited")

def get_key_value_from_string(string, key):
    if string[:len(key)] == key:
        return string[(len(key)+1):]
    else:
        return None