import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from linebot.models import *
import urllib.parse


def returnAnswer(userinput):
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


def gettemplate(dump):
    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                 thumbnail_image_url=f'{dump[0][1]}',
                 title=f'{dump[0][2]}',
                 text=f'{dump[0][3]}星\n{dump[0][4]}',
                 actions=[
                     PostbackAction(
                         label='postback1',
                         display_text='postback text1',
                         data='action=buy&itemid=1'
                     ),
                     MessageAction(
                         label='message1',
                         text='message text1'
                     ),
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
                        PostbackAction(
                         label='postback1',
                         display_text='postback text1',
                         data='action=buy&itemid=1'
                        ),
                        MessageAction(
                            label='message1',
                            text='message text1'
                        ),
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
                        PostbackAction(
                         label='postback1',
                         display_text='postback text1',
                         data='action=buy&itemid=1'
                        ),
                        MessageAction(
                            label='message1',
                            text='message text1'
                        ),
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
                        PostbackAction(
                         label='postback1',
                         display_text='postback text1',
                         data='action=buy&itemid=1'
                        ),
                        MessageAction(
                            label='message1',
                            text='message text1'
                        ),
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
                        PostbackAction(
                         label='postback1',
                         display_text='postback text1',
                         data='action=buy&itemid=1'
                        ),
                        MessageAction(
                            label='message1',
                            text='message text1'
                        ),
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
                        PostbackAction(
                         label='postback1',
                         display_text='postback text1',
                         data='action=buy&itemid=1'
                        ),
                        MessageAction(
                            label='message1',
                            text='message text1'
                        ),
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
                        PostbackAction(
                         label='postback1',
                         display_text='postback text1',
                         data='action=buy&itemid=1'
                        ),
                        MessageAction(
                            label='message1',
                            text='message text1'
                        ),
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
                        PostbackAction(
                         label='postback1',
                         display_text='postback text1',
                         data='action=buy&itemid=1'
                        ),
                        MessageAction(
                            label='message1',
                            text='message text1'
                        ),
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
                        PostbackAction(
                         label='postback1',
                         display_text='postback text1',
                         data='action=buy&itemid=1'
                        ),
                        MessageAction(
                            label='message1',
                            text='message text1'
                        ),
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
                        PostbackAction(
                         label='postback1',
                         display_text='postback text1',
                         data='action=buy&itemid=1'
                        ),
                        MessageAction(
                            label='message1',
                            text='message text1'
                        ),
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
