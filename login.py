import shutil

def print_dashes():
    dash = '-'

    try:
        column = shutil.get_terminal_size().columns

        print(dash * column)
    except OSError:
        print(dash * 97)

def print_equals():
    equal = '='

    try:
        column = shutil.get_terminal_size().columns

        print(equal * column)
    except OSError:
        print(equal * 97)

print_equals()