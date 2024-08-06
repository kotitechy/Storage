import os

def open_file(filename):
    os.system("xdg-open " + filename)  # For Linux
    # os.system("start " + filename)    # For Windows

open_file("output.mp3")