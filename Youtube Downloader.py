pip install pytube3

from pytube import YouTube

youtube = YouTube("https://youtu.be/SMYlmmHQ2IQ")

streams = youtube.streams

for i in streams:
    print(i)

print('\n\nVideo after extracting uisng specific information.')
filters = youtube.streams.filter(progressive = True, file_extension='mp4')

for i in filters:
    print("\n")
    print(i)

filters.get_highest_resolution().download(output_path='/Users/user10/desktop/youtube_downloads', filename='aash.mp4')

print('\nVideo Downloaded Successfully')

# if you want only audio of youtube video to be downloaded then use the method get_method_only()

filters.get_audio_only().download(output_path='/Users/user10/desktop/youtube_downloads', filename='aash.mp4')

# if you want mulltiple files to be downloaded then we can use a list containing multiple urls

urls = ["https://youtu.be/HzGE_WaSqE4", "https://youtu.be/PMCu0JtizCk"]

# if you want to download the whole playlist then we have an inbuilt function

from pytube import Playlist

playlist = Playlist(url)

playlist.download_all(download_path='/Users/pankaj/temp')