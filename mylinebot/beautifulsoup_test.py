from xml.dom.minidom import Attr
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from linebot.models import *
import urllib.parse
userinput = '台北市'
url = f"https://ifoodie.tw/explore/{userinput}/list"
ua = UserAgent()
headers = {'user-agent': ua.random}
htmlfile = requests.get(url, headers=headers)
soup = BeautifulSoup(htmlfile.text, "lxml")
data = soup.find(
"div", class_="jsx-3759983297 item-list").find_all('div', attrs={'data-id': True})
num = 0
answer = []
for row in data:
        if num >= 10:
                break
        num += 1
        title = row.find("div", class_="jsx-3292609844 title").a.text
        title = title.replace(' ', '-')
        score = row.find("div", class_="jsx-1207467136 text").text
        opentime = row.find("div", class_="jsx-3292609844 info").text
        address = row.find("div", class_="jsx-3292609844 address-row").text
        id = row['data-id']
        titleURI = urllib.parse.quote(title)
        uri = f'https://ifoodie.tw/restaurant/{id}-{titleURI}'

        # 避開第三筆之後會出現的lazyloaded
        if num >= 3:
                imgsrc = row.find(
                'div', attrs={'class': 'jsx-3292609844 restaurant-info'}).a.img['data-src']
        else:
                imgsrc = row.find(
                'div', attrs={'class': 'jsx-3292609844 restaurant-info'}).a.img['src']
        content = [num, imgsrc, title, score, opentime, uri, address]
        answer.append(content)
print(len(answer))