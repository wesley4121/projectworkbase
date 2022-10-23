# Create your views here.
from cProfile import label
from codecs import backslashreplace_errors
from pydoc import text
from types import NoneType
from unittest import result
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
from re import *
import re
from MyBot.claw import *
import json
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

selectionlist=[]
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

        for event in events:

            if isinstance(event, MessageEvent):  # ===============================如果有訊息事件

                print(f'message.text : {event.message.text}')

                line_bot_api.reply_message(event.reply_token,
                                           # MESSAGE__HERE
                                           messages=getQuickReply(
                                               userinput_city=event.message.text)
                                           )
            # ============================如果有POSTBACK事件
            elif isinstance(event, PostbackEvent):
                
                front = re.search(r'(\w+)&', event.postback.data).group(1)
                back = re.search(r'&(\w+)', event.postback.data).group(1)
                if front == 'city':
                    selectionlist.append(back)
                    line_bot_api.reply_message(event.reply_token,getQuickReply(postback_city=back)
                        )
                if front == 'local':  # 正則 找&以前
                    selectionlist.append(back)
                    print(selectionlist[0])

                    dump = returnClawAnswer(  # 爬資料
                        userinput_city=selectionlist[0],
                        userinput_local=selectionlist[1]
                    )
                    line_bot_api.reply_message(  # 回覆爬蟲資料
                        event.reply_token,
                        getCarouselTemplate(dump))

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
