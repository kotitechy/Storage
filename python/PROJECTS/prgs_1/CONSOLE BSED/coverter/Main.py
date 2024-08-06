import tkinter as tk

from mp3 import mp3
from mp4 import mp4
from playlist_mp3 import playlist_mp3
from playlist_mp4 import playlist_mp4


def command_p1():
    mp3_1  = mp3()
    print("MP3")
    mp3_1.win()

def command_p3():
    pl_mp4 = playlist_mp4()
    print("MP4 PLAYLIST")
    pl_mp4.win()

def command_p4():
    pl_mp3 = playlist_mp3()
    print("MP3 PLAYLIST")
    pl_mp3.win()

def command_p2():
    mp4_1  = mp4()
    print("MP4")
    mp4_1.win()


def command_p5():
    print("EXIT")
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Shiva")
root.geometry('500x500')

# Header label
header_label = tk.Label(root, text="YouTube Header")
header_label.pack(pady=10)

# Buttons with commands
button_p1 = tk.Button(root, text="MP3", command=command_p1)
button_p1.pack(pady=5)

button_p2 = tk.Button(root, text="Mp4", command=command_p2)
button_p2.pack(pady=5)

button_p3 = tk.Button(root, text="Mp4 Playlist", command=command_p3)
button_p3.pack(pady=5)

button_p4 = tk.Button(root, text="MP3 Playlist", command=command_p4)
button_p4.pack(pady=5)

button_p5 = tk.Button(root, text="Exit", command=command_p5)
button_p5.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
