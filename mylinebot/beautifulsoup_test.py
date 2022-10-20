from xml.dom.minidom import Attr
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from linebot.models import *
import urllib.parse

ua = UserAgent()
headers = {'user-agent' : ua.random}
url="https://ifoodie.tw/explore/%E5%8F%B0%E5%8C%97%E5%B8%82/list"
htmlfile=requests.get(url , headers=headers)
soup=BeautifulSoup(htmlfile.text,"lxml")
data =soup.find("div",class_="jsx-3759983297 item-list").find_all('div',attrs={'data-id':True})
num=0
answer =[]
for row in data:
        if num ==6 : break
        num+=1
        title=row.find("div",class_="jsx-3292609844 title").a.text
        score=row.find("div",class_="jsx-1207467136 text").text
        opentime=row.find("div",class_="jsx-3292609844 info").text
        address=row.find("div",class_="jsx-3292609844 address-row").text
        id = row['data-id']
        titleURI = urllib.parse.quote(title)
        uri = f'https://ifoodie.tw/restaurant/{id}-{titleURI}'
        ##避開lazyloaded
        if num >=3:
                imgsrc = row.find('div', attrs={'class':'jsx-3292609844 restaurant-info'}).a.img['data-src']
        else:
                imgsrc = row.find('div', attrs={'class':'jsx-3292609844 restaurant-info'}).a.img['src']
        
        content = [num,imgsrc,title, score, opentime,uri]
        answer.append(content)
        
            # answer += f'編號 ： {num} \n餐廳名稱：{title}\n推薦指數(滿分五分)：{score}\n開店時間：{opentime}\n地址：{address}\n資訊：{uri}\n\n'

        # print(uri)
        # print(id)
        # print("編號:",num)
        # print("餐廳名稱:",title)
        # print("推薦指數(滿分五分):",score)
        # print(opentime)
        # print("地址:",address)
        # print(imgsrc)
        # print()
print(uri)