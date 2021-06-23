import requests
from bs4 import BeautifulSoup
import json
import urllib


page = requests.get("https://apps.apple.com/de/app/telegram-messenger/id686449807")

if page.status_code == 200:
    content = page.content

    Data = {}

    DOMdocument = BeautifulSoup(content, 'html.parser')

    Data['Image'] = DOMdocument.find("meta",  property="og:image")['content']
    print('Beginning file download with urllib2...')
    print(Data["Image"])
    url = Data["Image"]
    urllib.request.urlretrieve(url, '1.png')
