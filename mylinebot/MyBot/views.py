# Create your views here.
from pydoc import text
from types import NoneType
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
import urllib.parse
from MyBot.claw import *
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
                dump = returnClawAnswer(event.message.text)

                    
                

                line_bot_api.reply_message(event.reply_token, getQuickReply())
                

        return HttpResponse()
    else:
        return HttpResponseBadRequest()



