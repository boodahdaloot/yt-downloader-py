from pytube import YouTube
import os

link = input("Enter the video link: ")
yt = YouTube(link)

# Gets the video title;
title = yt.title

# Gest all available streams for the video;
streams = yt.streams.all()

# Prints all available streams for the user to choose from;
for i in range(len(streams)):
    print(f'{i+1}. {streams[i]}')

# Gets user's choice for stream they want;
choice = int(input("Enter the number corresponding to the desired stream: "))

# Downloads chosen stream to a specific location on the device;
if not os.path.exists("videos"):
    os.mkdir("videos")
streams[choice-1].download("videos")

print(f'Download complete: {title}')


