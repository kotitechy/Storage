from pytube import Playlist
playlist = Playlist('https://youtube.com/playlist?list=PLoBDkJXxnuE75SR8c-iVfY7EQCwSE9YJJ&si=_pdu37cE685ByUbK')
for video in playlist.videos:
    video.streams.get_highest_resolution().download()
    try:
        print('trying to download')
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


