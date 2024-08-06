from pytube import YouTube

# Replace 'your_video_url' with the URL of the YouTube video you want to download
video_url = 'your_video_url'

# Create a YouTube object
a=input("Enter Url")
yt = YouTube(a)

# Get the highest resolution stream
video_stream = yt.streams.get_highest_resolution()

# Download the video
video_stream.download()

print(f"Video '{yt.title}' downloaded successfully.")
