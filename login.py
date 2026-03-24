import shutil

def print_dashes():
    dash = '-'

    try:
        column = shutil.get_terminal_size().columns

        print(dash * column)
    except OSError:
        print(dash * 97)

print_dashes()