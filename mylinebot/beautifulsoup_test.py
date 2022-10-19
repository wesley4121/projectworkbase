from email.mime import image
from operator import truediv
from xml.dom.minidom import Attr
import requests
from bs4 import BeautifulSoup
url="https://ifoodie.tw/explore/%E5%8F%B0%E5%8C%97%E5%B8%82/list"
htmlfile=requests.get(url)
soup=BeautifulSoup(htmlfile.text,"lxml")
# rows=soup.find("div",class_="jsx-3759983297 item-list").find_all("div",class_="jsx-3292609844 restaurant-info")
data =soup.find("div",class_="jsx-3759983297 item-list").find_all('div',attrs={'data-id':True})
# result = [item['data-id'] for item in soup.find_all('div', attrs={'data-id' : True})]
# print(result)
num=0
images = soup.find_all('div',attrs={'class':'jsx-3292609844 restaurant-info'})
print(images[0].a.img['src'])
for row in data:
        num+=1
        title=row.find("div",class_="jsx-3292609844 title").a.text
        score=row.find("div",class_="jsx-1207467136 text").text
        opentime=row.find("div",class_="jsx-3292609844 info").text
        address=row.find("div",class_="jsx-3292609844 address-row").text
        id = row['data-id']
        imgsrc = row.find('img',attrs={'data-src':True})
        uri = f'https://ifoodie.tw/restaurant/{id}-{title}'
        print(uri)
        print(id)
        print("編號:",num)
        print("餐廳名稱:",title)
        print("推薦指數(滿分五分):",score)
        print(opentime)
        print("地址:",address)
        print(row.div.a.img['data-src'])