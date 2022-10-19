import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent



def returnAnswer(userinput):
    # url="https://ifoodie.tw/explore/%E5%8F%B0%E5%8C%97%E5%B8%82/list"
    url = f"https://ifoodie.tw/explore/{userinput}/list"
    ua = UserAgent()
    headers = {'user-agent': ua.random}
    htmlfile = requests.get(url, headers=headers)
    soup = BeautifulSoup(htmlfile.text, "lxml")
    # rows=soup.find("div",class_="jsx-3759983297 item-list").find_all("div",class_="jsx-3292609844 restaurant-info")
    data = soup.find("div", class_="jsx-3759983297 item-list").find_all('div', attrs={'data-id': True})
    num = 0
    answer = []
    for row in data:
        if num == 6:
            break
        num += 1
        title = row.find("div", class_="jsx-3292609844 title").a.text
        title = title.replace(' ','-')
        score = row.find("div", class_="jsx-1207467136 text").text
        opentime = row.find("div", class_="jsx-3292609844 info").text
        address = row.find("div", class_="jsx-3292609844 address-row").text
        id = row['data-id']
        uri = f'https://ifoodie.tw/restaurant/{id}-{title}'

        # 避開第三筆之後會出現的lazyloaded
        if num >= 3:
            imgsrc = row.find(
                'div', attrs={'class': 'jsx-3292609844 restaurant-info'}).a.img['data-src']
        else:
            imgsrc = row.find(
                'div', attrs={'class': 'jsx-3292609844 restaurant-info'}).a.img['src']
        # answer += f'編號 ： {num} \n餐廳名稱：{title}\n推薦指數(滿分五分)：{score}\n開店時間：{opentime}\n地址：{address}\n資訊：{uri}\n\n'
        content = [num, imgsrc, title, score, opentime, uri]
        answer.append(content)

    return answer
returnAnswer('台北市')

