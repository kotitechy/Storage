from pytube import YouTube
import os

def download_youtube_audio(video_url):
    # Create a YouTube object
    yt = YouTube(video_url)

    # Get the highest quality audio stream
    audio_stream = yt.streams.filter(only_audio=True).first()

    # Construct the output path to the Downloads directory
    output_path = os.path.join(os.path.expanduser('~'), 'Downloads')

    # Create the Downloads directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    # Download the audio
    audio_stream.download(output_path)

    print(f"Audio from '{yt.title}' downloaded successfully as an MP3 file in the Downloads directory.")

# Take the YouTube URL as input from the user
video_url = input("Enter URL: ")

# Download the audio
download_youtube_audio(video_url)
