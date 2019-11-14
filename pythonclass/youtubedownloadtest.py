import pytube

url = 'https://www.youtube.com/watch?v=T1W0TLEit0Y'
pytube.YouTube(url).streams.first().download()