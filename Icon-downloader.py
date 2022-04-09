from os import X_OK, link, read
import requests
from bs4 import BeautifulSoup
import urllib
import numpy as np
from PIL import Image 
import shutil
import os



def downloader(a,b):
    link = a
    name = b
    path = "/mnt/c/Users/moonmind/Development/Android/Raphael-Icon-Pack/app/src/main/res/drawable-nodpi/"
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
#copy file
shutil.copyfile('drawable_base.xml', 'drawable_edit.xml')
file2 = open("drawable_edit.xml","a")


# Strips the newline character
for line in Lines:
    name = array_from_file[count]
    str1="\t<item drawable=\""
    str2="\n\n</resources>"
    str3="\" />\n"


    file2.writelines(str1)
    file2.writelines(name)
    file2.writelines(str3)

    count += 1
    downloader(line.strip(),name)

file2.writelines(str2)

file2.close()
file1.close()
#copy to app
shutil.copyfile('drawable_edit.xml','/mnt/c/Users/moonmind/Development/Android/Raphael-Icon-Pack/app/src/main/res/xml/drawable.xml')