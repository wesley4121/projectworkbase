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

                dump = returnClawAnswer(event.message.text)

                ct = TemplateSendMessage(
                    alt_text='Carousel template',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                thumbnail_image_url=f'https://example.com/bot/images/item1.jpg',
                                title=f'ddddd',
                                text=f'sasasasa',
                                actions=[
                                    MessageAction(
                                        label='message1',
                                        text='message text1'
                                    )


                                ]
                            )
                        ]
                    )
                )

                line_bot_api.reply_message(event.reply_token,
                                           getCarouselTemplate(dump)
                                           )

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
