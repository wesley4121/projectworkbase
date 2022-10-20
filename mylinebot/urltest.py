import time
import requests
url = 'https://www.google.com.tw/maps?hl=zh-TW&tab=wl'
htmlfile = requests.get(url=url)
print(htmlfile.url)
time.sleep(5)
print(htmlfile.url)
print(htmlfile.history)
