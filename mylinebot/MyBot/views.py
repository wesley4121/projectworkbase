# Create your views here.
from pydoc import text
from unittest import result
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):

    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:    # type: ignore
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                # BotResult = getuserInput(event.message.text)
                dump = returnAnswer(event.message.text) #[(0)num, (1)imgsrc, (2)title, (3)score, (4)opentime, (5)uri ,(6)address]
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
                                        uri='https://ifoodie.tw/restaurant/602dd8d802935e15f7b244bb-深紅汕頭鍋物-民權店'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                thumbnail_image_url='https://example.com/item2.jpg',
                                title='this is menu2',
                                text='description2',
                                actions=[
                                    PostbackAction(
                                        label='postback2',
                                        display_text='postback text2',
                                        data='action=buy&itemid=2'
                                    ),
                                    MessageAction(
                                        label='message2',
                                        text='message text2'
                                    ),
                                    URIAction(
                                        label='uri2',
                                        uri='http://example.com/2'
                                    )
                                ]
                            )
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token, carousel_template_message)
                

        return HttpResponse()
    else:
        return HttpResponseBadRequest()



def returnAnswer(userinput):
    url = f"https://ifoodie.tw/explore/{userinput}/list"
    ua = UserAgent()
    headers = {'user-agent': ua.random}
    htmlfile = requests.get(url, headers=headers)
    soup = BeautifulSoup(htmlfile.text, "lxml")
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
        content = [num, imgsrc, title, score, opentime, uri,address]
        answer.append(content)


    return answer

