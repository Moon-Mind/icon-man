from os import X_OK, link, read
import requests
from bs4 import BeautifulSoup
import urllib
from PIL import Image 
import os

def downloader(a,b):
    link = a
    path = "Icons/"
    count = str(b)
    #link = "https://apps.apple.com/de/app/google-drive-dateispeicher/id507874739"
    page = requests.get(link)
    if page.status_code == 200:
        content = page.content
        Data = {}
        DOMdocument = BeautifulSoup(content, 'html.parser')
        Data['Image'] = DOMdocument.find("meta",  property="og:image")['content']
        url = Data["Image"]
        name = link[30:33]
        urllib.request.urlretrieve(url, path+count+name+".png")
        im = Image.open(path+count+name+".png")
        im = im.crop((385, 100, 815, 530))
        im.save(path+count+name+".png")

    pass

# Using readlines()
file1 = open('links.txt', 'r')
Lines = file1.readlines()
count = 0

# Strips the newline character
for line in Lines:
    count += 1
    downloader(line.strip(),count)
