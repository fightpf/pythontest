import pytube
from tkinter import filedialog as fd

video_link='https://www.youtube.com/watch?v=T1W0TLEit0Y'
download_title=pytube.YouTube(video_link).title
print(download_title,len(download_title))
file = fd.asksaveasfile(mode='a',initialfile=download_title)
print(file.name)
location = file.name[0:len(file.name)-len(download_title)-4]
print(location)
#print(pytube.YouTube(video_link).streams.first))
#.download(location)

