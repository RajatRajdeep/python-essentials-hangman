import os

def clear_screen():
    command = "clear" if os.name == "posix" else "cls"
    os.system(command)