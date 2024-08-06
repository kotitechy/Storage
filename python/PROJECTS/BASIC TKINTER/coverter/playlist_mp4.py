from pytube import YouTube, Playlist
import os
import tkinter as tk

class playlist_mp4:
    @staticmethod
    def center_window(window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        window.geometry(f"{width}x{height}+{x}+{y}")

    def extract_video(self, playlist_url):
        # Create a Playlist object
        playlist = Playlist(playlist_url)

        # Get the path to the Downloads folder
        downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')

        # Use the sanitized playlist title as the subfolder name
        subfolder_name = self.sanitize_filename(playlist.title)

        # Create a subfolder within Downloads for YouTube video extraction
        output_path = os.path.join(downloads_path, subfolder_name)

        # Create the subfolder if it doesn't exist
        os.makedirs(output_path, exist_ok=True)

        print("Extracting Playlist Video")
        # Iterate through each video in the playlist
        for video_url in playlist.video_urls:
            yt = YouTube(video_url)
            try:
                # Get the highest resolution video stream
                video_stream = yt.streams.get_highest_resolution()
                # Download the video to the specified subfolder
                video_stream.download(output_path=output_path)
                print(f"Video '{yt.title}' extracted successfully to the '{subfolder_name}' folder in Downloads.")
            except Exception as e:
                print(e)

    def sanitize_filename(self, filename):
        # Replace characters not allowed in folder names with underscores
        invalid_chars = '\\/:*?"<>|'
        for char in invalid_chars:
            filename = filename.replace(char, '_')
        return filename

    def store_url(self):
        url = self.entry.get()  # Retrieve the entered URL from the Entry widget
        print("Entered URL:", url)
        self.extract_video(url)
        # You can now use the 'url' variable for further processing

    def win(self):
        # Create the main Tkinter window
        root = tk.Tk()

        # Set the window title
        root.title("YouTube Video Extractor")

        # Set the initial size of the window to 700x500 pixels
        window_width, window_height = 700, 500

        # Center the window on the screen
        self.center_window(root, window_width, window_height)

        # Set the background color of the window to blue
        root.configure(bg='LightBlue')

        # Create a header label with space at the top
        header_label = tk.Label(root, text="Youtube to mp4 playlist", font=('Arial', 20))

        # Create an Entry widget for entering the URL with space at the top
        self.entry = tk.Entry(root, width=50)

        # Create a button to trigger the URL storage function with space at the top
        button = tk.Button(root, text="Start mp3 Playlist Download", command=self.store_url)
        header_label.place(x=350, y=20, anchor='center')
        self.entry.place(x=200, y=100)
        button.place(x=200, y=150)

        # Start the Tkinter event loop
        root.mainloop()

# # Create an instance of the VideoExtractor class
# extractor = VideoExtractor()
#
# # Start the Tkinter window
# extractor.win()
