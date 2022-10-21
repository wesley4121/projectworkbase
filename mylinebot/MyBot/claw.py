from asyncio.windows_events import NULL
from ctypes.wintypes import PINT
from email import message
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from linebot.models import *
import urllib.parse

citys = ['台北市', '新北市', '桃園市', '台中市', '台南市', '高雄市', '基隆市', '宜蘭縣', '新竹市',
         '新竹縣', '苗栗縣', '彰化縣', '雲林縣', '嘉義市', '嘉義縣', '屏東縣', '花蓮縣', '南投縣',
         '台東縣', '澎湖縣', '金門縣']
sh = '台'

# str_match = [s for s in my_list if "ack" in s]
# print(str_match)
ctsanswer = []
for ct in citys:
    if ct.__contains__('市'):
        ctsanswer.append(ct)
        print(ct)
print(ctsanswer)
messageslist = []
messageslist.append(QuickReplyButton(
                    action=PostbackAction(
                        label=f"{citys[0]}", data=f"city&{citys[0]}")
                    ))

print( QuickReplyButton())


# if  not citys.__contains__('dd'):
#     print('t')


def returnClawAnswer(userinput):
    if not citys.__contains__(userinput):
        return None
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
        if num > 11:
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

    return answer


def getQuickReply(dump=None):
    quick_reply = TextSendMessage(
        text='a quick reply message',
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=PostbackAction(
                        label=f"{citys[0]}", data=f"city&{citys[0]}")
                )

            ]
        )
    )
    return quick_reply


# [num, imgsrc, title, score, opentime, uri, address]
def getCarouselTemplate(dump):
    if dump == None:
        return TextSendMessage(text='沒有資料')
    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=f'{dump[0][1]}',
                    title=f'{dump[0][2]}',
                    text=f'{dump[0][3]}星\n{dump[0][4]}',
                    actions=[
                        URIAction(
                            label='詳細',
                            uri=f'{dump[0][5]}'
                        ),
                        PostbackAction(
                            type="postback",
                            label="Position",
                            data="action=buy&itemid=111",
                            displayText="Position",

                        )

                    ]
                )
            ]
        )
    )
    return carousel_template_message
