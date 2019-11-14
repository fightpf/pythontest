from selenium import webdriver
driver = webdriver.Chrome('chromedriver')
driver.get('https://comicbus.live/online/manga_14132.html?ch=182')

from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'lxml')
print('https:' + soup.select_one('#TheImg').get('src'))

import requests
res = requests.get('https://img4.8comic.com/4/14132/182/001_89T.jpg')
with open('test.jpg', 'wb') as f:
    f.write(res.content)

from PIL import Image
Image.open('test.jpg')
pagenum = int(soup.select_one('#pagenum').text.split('/')[1].strip('頁'))
import time
pageurl = 'https://comicbus.live/online/manga_14132.html?ch=182-{}'
for i in range(pagenum):
    driver.get(pageurl.format(i+1))
    soup = BeautifulSoup(driver.page_source, 'lxml')
    imgurl = 'https:' + soup.select_one('#TheImg').get('src')
    print(imgurl)
    res = requests.get(imgurl)
    with open('{}.jpg'.format(i), 'wb') as f:
        f.write(res.content)
    time.sleep(1)