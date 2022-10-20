# python爬蟲結合LineBot

## requirement
`pip install django`  
`pip install fake_useragent`  
`pip install line-bot-sdk`  
`pip install beautifulsoup4`  

## installation

1. ngrok雲端伺服器    [ngrok](https://dashboard.ngrok.com/get-started/setup)  
1.下載並辦好帳號後開啟'ngrok.exe'  
2.輸入`ngrok config add-authtoken "你的帳號識別金鑰"`  
3.再輸入`ngrok http 8000`  

2. 找到`Forwarding`  
1.`https://--------隨機--------.au.ngrok.io`(網址每次啟動都會更換)  
2.`mylinebot\mylinebot\settings.py`裡面的`ALLOWED_HOSTS=[]`更換成`--------隨機--------.au.ngrok.io`  

3. LINEBOT-API    [developers](https://developers.line.biz/console/)  
1.新增一個`Provider`並創建`Messaging API`  
2.將`Basic settings`裡的`Channel secret` 填到`mylinebot\mylinebot\settings.py` 的`LINE_CHANNEL_SECRET =''`之中  
3.`Messaging API`裡的`Channel access token` 填到`LINE_CHANNEL_ACCESS_TOKEN =''`之中  
4.`Messaging API`裡的`Webhook URL`填入`https://--------隨機--------.au.ngrok.io/MyBot/callback`

4. 用`python .\manage.py runserver`在該目錄底下啟動`manage.py`  
1.到`Messaging API`裡的`Webhook settings`的`Verify` 出現`Success` 代表成功






