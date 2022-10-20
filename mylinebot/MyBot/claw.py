from asyncio.windows_events import NULL
from ctypes.wintypes import PINT
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from linebot.models import *
import urllib.parse

citys = ['台北市', '新北市', '桃園市', '台中市', '台南市', '高雄市', '基隆市', '宜蘭縣', '新竹市',
         '新竹縣', '苗栗縣', '彰化縣', '雲林縣', '嘉義市', '嘉義縣', '屏東縣', '花蓮縣', '南投縣',
         '台東縣', '澎湖縣', '金門縣']


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
                    action=CameraAction(label="開啟相機吧")
                ),
                QuickReplyButton(
                    action=CameraRollAction(label="相機膠捲")
                ),
                # return a location message
                QuickReplyButton(
                    action=LocationAction(label="位置資訊")
                ),
                QuickReplyButton(
                    action=PostbackAction(label="postback", data="postback")
                ),
                QuickReplyButton(
                    action=MessageAction(label="message", text="one message")
                ),
                QuickReplyButton(
                    action=DatetimePickerAction(label="時間選單",
                                                data="date_postback",
                                                mode="date",
                                                max='2022-06-18',
                                                min='2010-06-18'
                                                )
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
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=f'{dump[1][1]}',
                    title=f'{dump[1][2]}',
                    text=f'{dump[1][3]}星\n{dump[1][4]}',
                    actions=[
                        URIAction(
                            label='詳細',
                            uri=f'{dump[1][5]}'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=f'{dump[2][1]}',
                    title=f'{dump[2][2]}',
                    text=f'{dump[2][3]}星\n{dump[2][4]}',
                    actions=[
                        URIAction(
                            label='詳細',
                            uri=f'{dump[2][5]}'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=f'{dump[3][1]}',
                    title=f'{dump[3][2]}',
                    text=f'{dump[3][3]}星\n{dump[3][4]}',
                    actions=[
                        URIAction(
                            label='詳細',
                            uri=f'{dump[3][5]}'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=f'{dump[4][1]}',
                    title=f'{dump[4][2]}',
                    text=f'{dump[4][3]}星\n{dump[4][4]}',
                    actions=[
                        URIAction(
                            label='詳細',
                            uri=f'{dump[4][5]}'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=f'{dump[5][1]}',
                    title=f'{dump[5][2]}',
                    text=f'{dump[5][3]}星\n{dump[5][4]}',
                    actions=[
                        URIAction(
                            label='詳細',
                            uri=f'{dump[5][5]}'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=f'{dump[6][1]}',
                    title=f'{dump[6][2]}',
                    text=f'{dump[6][3]}星\n{dump[6][4]}',
                    actions=[
                        URIAction(
                            label='詳細',
                            uri=f'{dump[6][5]}'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=f'{dump[7][1]}',
                    title=f'{dump[7][2]}',
                    text=f'{dump[7][3]}星\n{dump[7][4]}',
                    actions=[
                        URIAction(
                            label='詳細',
                            uri=f'{dump[7][5]}'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=f'{dump[8][1]}',
                    title=f'{dump[8][2]}',
                    text=f'{dump[8][3]}星\n{dump[8][4]}',
                    actions=[
                        URIAction(
                            label='詳細',
                            uri=f'{dump[8][5]}'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=f'{dump[9][1]}',
                    title=f'{dump[9][2]}',
                    text=f'{dump[9][3]}星\n{dump[9][4]}',
                    actions=[
                        URIAction(
                            label='詳細',
                            uri=f'{dump[9][5]}'
                        )
                    ]
                )

            ]
        )
    )
    return carousel_template_message
