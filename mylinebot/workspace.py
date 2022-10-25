from cgitb import text
from distutils.command.clean import clean
import re
from linebot.models import *
# test = "https://www.google.com/maps/embed/v1/place?key=AIzaSyC-xVxgi7ApeuFIelqPN4RANnZM2UkMltA&q=25.054353,121.5469941"

# newcls = re.search(r"=(\d+.*\d*)",test)
# # pos = newcls.group(0).replace('=','')
# pos2 = newcls.group(1).split(',')
# # print(pos)
# print(pos2[0])
# print(pos2[1])
# print(newcls.group(1))


# TextSendMessage( 
#         text='請點選',
#         quick_reply=QuickReply(
#             items=[
#             QuickReplyButton(
#                 action=PostbackAction(
#                     label=f"{lc_scan_answer[i]}",
#                     data=f"local&{lc_scan_answer[i]}",
#                     display_text=f'{lc_scan_answer[i]}'
#                 )
#             )
#             for i in range(len(lc_scan_answer))
#         ]
#         )
# )

# TextSendMessage( 
#         text='請點選',
#         quick_reply=QuickReply(
#             items=[
#             QuickReplyButton(
#                 action=PostbackAction(
#                     label=f"{lc_scan_answer[i]}",
#                     data=f"local&{lc_scan_answer[i]}",
#                     display_text=f'{lc_scan_answer[i]}'
#                 )
#             )
#             for i in range(len(lc_scan_answer))
#         ]
#         )
# )

alist = ['wwe','zxczxc','5454']
xczxczcx = ['wwe','uuuuuuuuuuuuuuu','5454']
print(xczxczcx+alist)