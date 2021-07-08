from os import X_OK, link, read
import requests
from bs4 import BeautifulSoup
import urllib
import numpy as np
from PIL import Image 
import os


name = "test"

def downloader(a,b):
    link = a
    name = b
    path = "Icons/"
    #link = "https://apps.apple.com/de/app/google-drive-dateispeicher/id507874739"
    page = requests.get(link)
    if page.status_code == 200:
        content = page.content
        Data = {}
        DOMdocument = BeautifulSoup(content, 'html.parser')
        Data['Image'] = DOMdocument.find("meta",  property="og:image")['content']
        url = Data["Image"]

        urllib.request.urlretrieve(url, path+name+".png")
        im = Image.open(path+name+".png")
        im = im.crop((385, 100, 815, 530))
        
        im.save(path+name+".png")


    pass


# Using readlines()
file1 = open('links.txt', 'r')
array_from_file = np.loadtxt("name.txt", dtype=str)

        
Lines = file1.readlines()
count = 0


# Strips the newline character
for line in Lines:
    name = array_from_file[count]
    count += 1
    downloader(line.strip(),name)
