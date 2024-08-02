import settings as s
import menus as m

if __name__ == '__main__':
    settings = s.get_settings()
    m.main_menu(settings)
    #print(f'''input={settings.paths.input}
#output={settings.paths.output}
#edited={settings.paths.edited}
#mode={settings.mode}''')