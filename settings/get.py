from settings.controller import Paths

def get_core_path():
    return "./settings/settings.txt"

def get_paths(core_path: str, paths_obj: Paths):
    with open(core_path, "rt") as settings_file:
        settings_list = []
        while(setting := settings_file.readline()):
            settings_list.append(setting)
        for setting in settings_list:
            Paths.input = get_input(setting)
            # Paths.output = get_output(setting)
            # Paths.edited = get_edited(setting)

def get_input(setting):
    if setting[:5] == 'input':
        return setting[6:]
    else:
        return None