
# Create your views here.
from unittest import result
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):

    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)  # 傳入的事件
            print(events)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:    # type: ignore
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                BotResult = getuserInput(event.message.text)
                line_bot_api.reply_message(  # 回復傳入的訊息文字
                    event.reply_token,
                    TextSendMessage(text=BotResult)
                )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()

def getuserInput(input):
    # url="https://ifoodie.tw/explore/%E5%8F%B0%E5%8C%97%E5%B8%82/list"
    url=f"https://ifoodie.tw/explore/{input}/list"
    htmlfile=requests.get(url)
    soup=BeautifulSoup(htmlfile.text,"lxml")
    rows=soup.find("div",class_="jsx-3759983297 item-list").find_all("div",class_="jsx-3292609844 restaurant-info") 
    num=0
    answer = ''
    for row in rows:
            num+=1
            title=row.find("div",class_="jsx-3292609844 title").a.text
            score=row.find("div",class_="jsx-1207467136 text").text
            opentime=row.find("div",class_="jsx-3292609844 info").text
            address=row.find("div",class_="jsx-3292609844 address-row").text
            print("編號:",num)
            print("餐廳名稱:",title)
            print("推薦指數(滿分五分):",score)
            print(opentime)
            print("地址:",address)
            print()
            answer += f'編號 ： {num} \n餐廳名稱：{title}\n推薦指數(滿分五分)：{score}\n開店時間：{opentime}\n地址：{address}\n\n'
    return answer
        