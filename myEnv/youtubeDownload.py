from pytubefix import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeStream = youtubeObject.streams.get_highest_resolution()
    try:
        if youtubeObject is not None:
            print(f"Downloading: {youtubeObject.title} ({youtubeStream.resolution})")
            youtubeStream.download()
    except Exception as e:
        print("An error has occurred: ", e)

    print("✅ Download complete")


link = input("Enter the YouTube video URL: ")
Download(link)