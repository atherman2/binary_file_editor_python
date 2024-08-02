from settings.classes import Paths
from settings.classes import Settings

def get_core_path(paths_obj: Paths):
    paths_obj.settings = "./settings/settings.txt"

def get_attributes(settings_obj: Settings):
    with open(settings_obj.paths.settings, "rt") as settings_file:
        
        settings_list = []
        
        while(setting := settings_file.readline()):
            setting = setting[:len(setting) - 1]
            settings_list.append(setting)
        
        for setting in settings_list:
            if settings_obj.paths.input == None:
                settings_obj.paths.input = get_key_value_from_string(setting, "input")
        
            if settings_obj.paths.output == None:
                settings_obj.paths.output = get_key_value_from_string(setting, "output")
        
            if settings_obj.paths.edited == None:
                settings_obj.paths.edited = get_key_value_from_string(setting, "edited")
            
            if settings_obj.mode == None:
                settings_obj.mode = get_key_value_from_string(setting, "mode")

def get_key_value_from_string(string, key):
    if string[:len(key)] == key:
        return string[(len(key)+1):]
    else:
        return None