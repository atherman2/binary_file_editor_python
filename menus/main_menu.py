from menus.edit_menu import edit_menu

def main_menu(settings):
    restart = True
    while (restart):
        option = input(f'''/// Enter the desired option:
          (1) - Edit (View/Write) //TODO
          (2) - View //TODO
          (3) - Write //TODO
          (4) - Script //TODO
        
          (0) - Exit program
          
>>> ''')

        print()

        match option:
            case "1":
                file = open(settings.paths.edited, 'r+b')
                restart = edit_menu(file)
                file.close()
            case "0":
                restart = False