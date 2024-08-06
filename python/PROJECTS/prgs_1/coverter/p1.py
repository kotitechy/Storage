from pytube import YouTube
urls = ["https://www.youtube.com/watch?v=I8zh8dIbtvo","https://www.youtube.com/watch?v=hDbgZde_REs","https://www.youtube.com/watch?v=WF4qdERIhW4","https://www.youtube.com/watch?v=IB-RJU74sKY","https://www.youtube.com/watch?v=0yMGH-0T2wM","https://www.youtube.com/watch?v=WSkzTswC69E","https://www.youtube.com/watch?v=jLXd6D7Mp6Y","https://www.youtube.com/watch?v=YvwZkQdc46k","https://www.youtube.com/watch?v=BDkkvX76Qtw","https://www.youtube.com/watch?v=qnMgfM90aZc","https://www.youtube.com/watch?v=foffKHd4pqU","https://www.youtube.com/watch?v=XtsoAjgUKmY","https://www.youtube.com/watch?v=IxIG_u9u3aE","https://www.youtube.com/watch?v=MeCaZmyznRw"]

for i in urls :
    yt = YouTube(i)
    print("ok ababu ",i)
    # Get the highest resolution stream
    video_stream = yt.streams.get_highest_resolution()

    # Download the video
    video_stream.download()

    print(f"Video '{yt.title}' downloaded successfully.")





# # Display the organized list of video URLs
# for i, video_url in enumerate(urls, start=1):
#     print(f"{i}. {video_url}")
