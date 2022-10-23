
import re
from linebot.models import *
test = "https://www.google.com/maps/embed/v1/place?key=AIzaSyC-xVxgi7ApeuFIelqPN4RANnZM2UkMltA&q=25.054353,121.5469941"

newcls = re.search(r"=(\d+.*\d*)",test)
# pos = newcls.group(0).replace('=','')
pos2 = newcls.group(1).split(',')
# print(pos)
print(pos2[0])
print(pos2[1])
print(newcls.group(1))


# citys = ['台北市', '新北市', '桃園市', '台中市', '台南市', '高雄市', '基隆市', '宜蘭縣', '新竹市',
#          '新竹縣', '苗栗縣', '彰化縣', '雲林縣', '嘉義市', '嘉義縣', '屏東縣', '花蓮縣', '南投縣',
#          '台東縣', '澎湖縣', '金門縣']
# ct_scan_answer = []
# for ct in citys:
#     if ct.__contains__('縣'):
#         ct_scan_answer.append(ct)
# print(ct_scan_answer)
# print()

# quick_itemList = []
# testlist = [QuickReplyButton(action=PostbackAction(label=f"{ct}",data=f"city&{ct}")) for i in range(12)]
# for ct in ct_scan_answer:
#     quick_itemList.append(
#         QuickReplyButton(
#             action=PostbackAction(
#                 label=f"{ct}",
#                 data=f"city&{ct}"
#             )
#         )
#     )
# print(quick_itemList)
# print()
# print()
# print(testlist)
# quickreply = TextSendMessage(
#     text='a quick reply message',
#     quick_reply=QuickReply(
#         items=quick_itemList
#     )
# )
