from bs4 import BeautifulSoup
import requests
import pandas as pd 

w="https://open.spotify.com/section/0JQ5DB5E8N831KzFzsBBQ2"

request=requests.get(w)
print(request.status_code)

sp=BeautifulSoup(request.text,"html.parser")

sname=sp.find_all(class_="CardTitle__LineClamp-sc-1h38un4-0 RBShQ")

sbc=sname.find_all('span', recursive=False)
print(sbc)