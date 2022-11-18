from ast import Try
from types import NoneType
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from linebot.models import *
import urllib.parse
from MyBot.TaiwanCitys import *
from MyBot.location import *

citys = ['台北市', '新北市', '桃園市', '台中市', '台南市', '高雄市', '基隆市', '宜蘭縣', '新竹市',
         '新竹縣', '苗栗縣', '彰化縣', '雲林縣', '嘉義市', '嘉義縣', '屏東縣', '花蓮縣', '南投縣',
         '台東縣', '澎湖縣', '金門縣']

locals = area_data


types = ['新開幕', '火鍋', '早午餐', '小吃', '餐酒館', '酒吧', '精緻高級', '約會餐廳', '甜點', '燒烤', '日本料理', '居酒屋', '義式料理',
         '中式料理', '韓式', '泰式', '港式料理', '美式', '冰品飲料', '蛋糕', '飲料店', '吃到飽', '合菜', '牛肉麵', '牛排', '咖啡', '素食',
         '寵物友善', '景觀餐廳', '親子餐廳', '拉麵', '咖哩', '宵夜', '早餐', '午餐', '晚餐', '下午茶']



def returnClawAnswer(userinput_city=None, userinput_local=None, userinput_type=None , location=None):  # 爬蟲主程式

    if not userinput_city == None and not userinput_local == None and not userinput_type == None:

        url = f"https://ifoodie.tw/explore/{userinput_city}/{userinput_local}/list/{userinput_type}"

    elif not userinput_city == None and not userinput_local == None:

        url = f"https://ifoodie.tw/explore/{userinput_city}/{userinput_local}/list"

    elif not location == None:

        url = f"https://ifoodie.tw/explore/list?place=current&latlng={location[0]},{location[1]}"

    else:

        url = f"https://ifoodie.tw/explore/{userinput_city}/list"

    ua = UserAgent()
    headers = {'user-agent': ua.random}
    htmlfile = requests.get(url, headers=headers)
    soup = BeautifulSoup(htmlfile.text, "lxml")

    data = soup.find(
        "div", class_="jsx-3759983297 item-list").find_all('div', attrs={'data-id': True})
    num = 0
    answer = []
    for row in data:
        score = None
        title = None
        opentime = None
        address = None
        id = None
        location = None
        if num >= 10:
            break
        num += 1
        try:
            title = row.find("div", class_="jsx-3292609844 title").a.text
            title = title.replace(' ', '-')  # 取代空白
        except:
            if title == None:
                title = '無資料'
        try:
            score = row.find("div", class_="jsx-1207467136 text").text
        except:
            if score == None:
                score = '無資料'
        try:
            opentime = row.find("div", class_="jsx-3292609844 info").text
        except:
            if opentime == None:
                opentime = '無資料'
        try:
            address = row.find("div", class_="jsx-3292609844 address-row").text
        except:
            if address == None:
                address = '無資料'
        try:
            id = row['data-id']
        except:
            if id == None:
                id = '無資料'
        try:
            titleURI = urllib.parse.quote(title)  # 轉URI
        except:
            if titleURI == None:
                titleURI = '無資料'
        try:
            uri = f'https://ifoodie.tw/restaurant/{id}-{titleURI}'  # 詳細資料
        except:
            if uri == None:
                uri = '無資料'
        try:
            location = returnLocation(uri)
        except:
            if location == None:
                location = '無資料'
        if num >= 3:
            imgsrc = row.find(
                'div', attrs={'class': 'jsx-3292609844 restaurant-info'}).a.img['data-src']
        else:
            imgsrc = row.find(
                'div', attrs={'class': 'jsx-3292609844 restaurant-info'}).a.img['src']
        content = [num, imgsrc, title, score, opentime,
                   uri, address, location[0], location[1]]
        answer.append(content)

    return answer


#===================================================================================================================
#===================================================================================================================
def getQuickReply(userinput_city=None, postback_city=None, postback_pagechange=None):  # 快速回覆
    if not userinput_city == None:  # 接收使用者輸入

        ct_scan_answer = []
        for ct in citys:  # 如果CT中有輸入的資料裝進SCANLIST
            if ct.__contains__(userinput_city):
                ct_scan_answer.append(ct)
        if len(ct_scan_answer) == 0:  # 如果LIST為0則為沒有資料
            return TextSendMessage(text='沒有資料')
        nowlocation = [
            QuickReplyButton(
                image_url='https://cdn-icons-png.flaticon.com/128/4481/4481066.png',
                action=LocationAction(
                    label=f"鄰近位置"

                )
            )
        ]
        quick_itemList = nowlocation + [  # 創建ITEMLIST 放進資料
            QuickReplyButton(
                image_url='https://cdn-icons-png.flaticon.com/128/4619/4619003.png',
                action=PostbackAction(
                    label=f"{ct_scan_answer[i]}",
                    data=f"city&{ct_scan_answer[i]}",
                    display_text=f'{ct_scan_answer[i]}'
                )
            )
            for i in range(len(ct_scan_answer))
        ]
#===================================================================================================================
    if not postback_city == None :  # 　postback_city = 接收使用者按下按鈕的POSTBACK

        lc_scan_answer = locals[f'{postback_city}']
        
        if len(lc_scan_answer) > 10:
            nowlocation = [
                QuickReplyButton(
                    image_url='https://cdn-icons-png.flaticon.com/128/4481/4481066.png',
                    action=LocationAction(
                        
                        label=f"鄰近位置"
                        
                    )
                )
            ]
            uppage_button = [
                QuickReplyButton(
                    image_url='https://cdn-icons-png.flaticon.com/128/4495/4495685.png',
                    action=PostbackAction(
                        
                        label=f"上一頁",
                        data=f'page&up,{postback_city}'
                    )
                )
            ]
            downpage_button = [
                QuickReplyButton(
                    image_url='https://cdn-icons-png.flaticon.com/128/4495/4495689.png',
                    
                    action=PostbackAction(
                        label=f"下一頁",
                        data=f'page&down,{postback_city}'
                    )
                )
            ]
            quick_item_pagelist = [
                [
                    QuickReplyButton(
                    image_url='https://cdn-icons-png.flaticon.com/128/4619/4619069.png',
                        action=PostbackAction(
                            label=f"{lc_scan_answer[i]}",
                            data=f"local&{lc_scan_answer[i]}",
                            display_text=f'{lc_scan_answer[i]}'
                        )
                    )
                    for i in range(9)
                ],
                [
                    QuickReplyButton(
                        image_url='https://cdn-icons-png.flaticon.com/128/4619/4619069.png',
                        action=PostbackAction(
                            label=f"{lc_scan_answer[i+9]}",
                            data=f"local&{lc_scan_answer[i+9]}",
                            display_text=f'{lc_scan_answer[i+9]}'
                        )
                    )
                    for i in range(len(lc_scan_answer)-9)
                ]
            ]
            quick_itemList = downpage_button + nowlocation + quick_item_pagelist[0]

        elif  len(lc_scan_answer) <= 10:
            quick_itemList = [
                QuickReplyButton(
                    image_url='https://cdn-icons-png.flaticon.com/128/4619/4619069.png',    
                    action=PostbackAction(
                        label=f"{lc_scan_answer[i]}",
                        data=f"local&{lc_scan_answer[i]}",
                        display_text=f'{lc_scan_answer[i]}'
                    )
                )
                for i in range(len(lc_scan_answer))
            ]
#===================================================================================================================
        
    if not postback_pagechange == None:

        postback_pagechange_data_slice = postback_pagechange.split(',')
        print(postback_pagechange_data_slice[0])
        print(postback_pagechange_data_slice[1])
        lc_scan_answer = locals[f'{postback_pagechange_data_slice[1]}']
        nowlocation = [
            QuickReplyButton(
                image_url='https://cdn-icons-png.flaticon.com/128/4481/4481066.png',
                action=LocationAction(
                    label=f"鄰近位置"
                    
                )
            )
        ]
        uppage_button = [
            QuickReplyButton(
                image_url='https://cdn-icons-png.flaticon.com/128/4495/4495685.png',
                action=PostbackAction(
                    label=f"上一頁",
                    data=f'page&up,{postback_pagechange_data_slice[1]}'
                )
            )
        ]
        downpage_button = [
            QuickReplyButton(
                image_url='https://cdn-icons-png.flaticon.com/128/4495/4495689.png',
                
                action=PostbackAction(
                    label=f"下一頁",
                    data=f'page&down,{postback_pagechange_data_slice[1]}'
                )
            )
        ]
        quick_item_pagelist = [
            [
                QuickReplyButton(
                    image_url='https://cdn-icons-png.flaticon.com/128/4619/4619069.png',
                    action=PostbackAction(
                        label=f"{lc_scan_answer[i]}",
                        data=f"local&{lc_scan_answer[i]}",
                        display_text=f'{lc_scan_answer[i]}'
                    )
                )
                for i in range(9)
            ],
            [
                QuickReplyButton(
                    image_url='https://cdn-icons-png.flaticon.com/128/4619/4619069.png',
                    action=PostbackAction(
                        label=f"{lc_scan_answer[i+9]}",
                        data=f"local&{lc_scan_answer[i+9]}",
                        display_text=f'{lc_scan_answer[i+9]}'
                    )
                )
                for i in range(len(lc_scan_answer)-9)
            ]
        ]
        if postback_pagechange_data_slice[0] =='up':
            quick_itemList = downpage_button + nowlocation + quick_item_pagelist[0]
        elif postback_pagechange_data_slice[0] == 'down':
            quick_itemList = uppage_button + nowlocation + quick_item_pagelist[1]
#===================================================================================================================
    quickreply = TextSendMessage(  # 裝進TEXT_MESSAGE
        text='請點選',
        quick_reply=QuickReply(
            items=quick_itemList
        )
    )
    return quickreply
#===================================================================================================================
#===================================================================================================================


# [num, imgsrc, title, score, opentime, uri, address, location[0],location[1]]
def getCarouselTemplate(dump=None):
    if dump == None:
        return TextSendMessage(text='沒有資料')
        
    columnlist = [
        CarouselColumn(
            thumbnail_image_url=f'{dump[i][1]}',
            title=f'{dump[i][2]}',
            text=f'{dump[i][3]}星\n{dump[i][4]}',
            actions=[
                URIAction(
                    label='詳細',
                    uri=f'{dump[i][5]}'
                ),
                PostbackAction(
                    label=f"位置",
                    data=f"location&{dump[i][2]},{dump[i][6]},{dump[i][7]},{dump[i][8]}",
                )
            ]
        )
        for i in range(len(dump))
    ]
    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=columnlist
        )
    )
    return carousel_template_message
#===================================================================================================================
#===================================================================================================================
