def edit_menu(file):
    restart = True
    pos = file.tell()
    viewing_buffer = ""
    while (restart):
        option = input(f'''/// Current mode: edit(view/write)
/// Current pos = {pos}
/// Viewing buffer:

{viewing_buffer}

/// Choose what to do next:
          (1) - View
          (2) - Write //TODO
          (3) - Seek //TODO
          (4) - Script //TODO
        
          (0) - Exit program
          
>>> ''')

        print()

        match option:
            case "1":
                viewing_buffer = view_menu(file)
            case "0":
                restart = False