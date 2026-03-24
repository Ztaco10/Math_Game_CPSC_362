import shutil

def print_dashes():
    dash = '-'

    try:
        column = shutil.get_terminal_size().column

        print(dash * column)
    except OSError:
        print(dash * 80)