from pytube import YouTube
import os
import tkinter as tk

class mp3:
    @staticmethod
    def center_window(window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        window.geometry(f"{width}x{height}+{x}+{y}")

    def download(self, url_o):
        # Create a YouTube object
        yt = YouTube(url_o)

        # Get the highest quality audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Construct the output path to the Downloads directory
        output_path = os.path.join(os.path.expanduser('~'), 'Downloads')

        # Create the Downloads directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)

        print("DOWNLOADING")
        # Download the audio
        audio_stream.download(output_path)

        print(f"Audio from '{yt.title}' downloaded successfully as an MP3 file in the Downloads directory.")

    def store_url(self):
        url = self.entry.get()  # Retrieve the entered URL from the Entry widget
        print("Entered URL:", url)
        self.download(url)
        # You can now use the 'url' variable for further processing

    def win(self):
        # Create the main Tkinter window
        root = tk.Tk()

        # Set the window title
        root.title("Window with Image Background")

        # Set the initial size of the window to 700x500 pixels
        window_width, window_height = 700, 500

        # Center the window on the screen
        self.center_window(root, window_width, window_height)

        # Set the background color of the window to blue
        root.configure(bg='LightBlue')

        # Create a header label with space at the top
        header_label = tk.Label(root, text="Youtube to mp3", font=('Arial', 20))

        # Create an Entry widget for entering the URL with space at the top
        self.entry = tk.Entry(root, width=50)

        # Create a button to trigger the URL storage function with space at the top
        button = tk.Button(root, text="Download Audio", command=self.store_url)
        header_label.place(x=350, y=20, anchor='center')
        self.entry.place(x=200, y=100)
        button.place(x=200, y=150)

        # Start the Tkinter event loop
        root.mainloop()
#
# # Create an instance of the mp3 class
# mp = mp3()
#
# # Start the Tkinter window
# mp.win()
