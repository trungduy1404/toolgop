from urllib.parse import quote
import datetime
import os
import ssl
from urllib.parse import urlencode
from http import cookiejar
from urllib3.exceptions import InsecureRequestWarning
import hashlib
import random
import os
import requests
import random
import time
from bs4 import BeautifulSoup
import re
from time import sleep
import sys
import requests,sys
from time import sleep
from datetime import timedelta
try:
    import base64
    from requests.exceptions import RequestException
    import requests
    import pystyle
    from concurrent.futures import ThreadPoolExecutor
    from faker import Faker
    from requests import session
    import concurrent.futures
    import prettytable
    
except ImportError:
    import os
    os.system("pip install faker")
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install pystyle")
    os.system("pip install concurrent.futures")
    os.system("pip install base64")
import requests,os,time,re,json,uuid,random,sys
from concurrent.futures import ThreadPoolExecutor
import datetime
from datetime import datetime
import requests,json
import uuid
import requests
from time import sleep
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from pystyle import Colors, Colorate, Write, Center, Add, Box
from time import sleep,strftime
import socket
from pystyle import *
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ndp_delay_tool(p):
    while p > 1:
        p = p - 1
        print(f'\033[1;31m[ ❤❤ ANH LÀ TRUNG DUY ❤❤ ][-][..............][{p}]', '     ', end='\r')
        sleep(1 / 6)
        print(f'\033[1;32m[ 💌 ĐANG KẾT NỐI 💌 ][+][Đ.............][{p}]', '     ', end='\r')
        sleep(1 / 6)
        print(f'\033[1;33m[ ❤❤ VUI LÒNG ĐỢI ❤❤ ][|][ĐA............][{p}]', '     ', end='\r')
        sleep(1 / 6)
        print(f'\033[1;34m[ 💌 ANH LÀ TRUNG DUY 💌 ][/][ĐANG..........][{p}]', '     ', end='\r')
        sleep(1 / 6)
        print(f'\033[1;35m[ ❤❤ ĐANG KẾT NỐI ❤❤ ][-][ĐANG K........][{p}]', '     ', end='\r')
        sleep(1 / 6)
        print(f'\033[1;36m[ 💌 VUI LÒNG ĐỢI 💌 ][+][ĐANG KẾT......][{p}]', '     ', end='\r')
        sleep(1 / 6)
        print(f'\033[1;37m[ ❤❤ ANH LÀ TRUNG DUY ❤❤ ][\][ĐANG KẾT N....][{p}]', '     ', end='\r')
        sleep(1 / 6)
        print(f'\033[1;38m[ 💌 ĐANG KẾT NỐI💌 ][|][ĐANG KẾT NỐI..][{p}]', '     ', end='\r')
        sleep(1 / 6)
        print(f'\033[1;33m[ ❤❤ VUI LÒNG ĐỢI ❤❤ ][|][Đ.............][{p}]', '     ', end='\r')
        sleep(1 / 6)
        os.system("cls" if os.name == "nt" else "clear")
p = random.randint(1, 10)
ndp_delay_tool(p)
def runbanner(text, delay=0.001):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    
#import lại sau khi cài đặt
from faker import Faker
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import requests

trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam = '\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hongnhat = "#FFC0CB"
kt_code = "</>"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"

colors = [
    "\033[1;37m\033[1m",  # Trắng
    "\033[1;32m\033[1m",  # Xanh lá
    "\033[1;34m\033[1m",  # Xanh dương
    "\033[1m\033[38;5;51m",  # Xanh nhạt
    "\033[1;31m\033[1m\033[1m",  # Đỏ
    "\033[1;30m\033{1m",  # Xám
    "\033[1;33m\033[1m",  # Vàng
    "\033[1;35m\033[1m",  # Tím
    "\033[32;5;245m\033[1m\033[38;5;39m",  # Màu đặc biệt
]

os.system('cls' if os.name == 'nt' else 'clear')

banner = """
\033[1;33m╔═════════════════════════════════════════════════════════════════════════════════╗
\033[1;33m║\033[1;35m ████████╗██████╗░██╗░░░██╗██╗░░░██╗████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
  ╚══██╔══╝██╔══██╗██║░░░██║╚██╗░██╔╝╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
  ░░░██║░░░██║░░██║██║░░░██║░╚████╔╝░░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
  ░░░██║░░░██║░░██║██║░░░██║░░╚██╔╝░░░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
  ░░░██║░░░██████╔╝╚██████╔╝░░░██║░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
  ░░░╚═╝░░░╚═════╝░░╚═════╝░░░░╚═╝░░░-░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░
\033[1;33m╠═════════════════════════════════════════════════════════════════════════════════╣
\033[1;33m║\033[1;34m▶ Nhóm Gmail  : \033[1;35mboladuy4@gmail.com            \033[1;33m║
\033[1;33m║\033[1;34m▶ FaceBook : \033[1;35m https://www.facebook.com/trungduycutodz          \033[1;33m║
\033[1;33m║\033[1;34m▶ Tool Vip : \033[1;35mTrung Duy Deocode                          \033[1;33m║
\033[1;33m║\033[1;34m▶ Bạn Không Ngu, Do Tôi Quá Giỏi               \033[1;33m║
\033[1;33m╚═══════════════════════════════════════════════╝
\033[1;32m-------------------------------------------------"""
print(banner)
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║     \033[1;39mWar Mess      \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m1.1\033[1;31m] \033[1;32mTOOL TREO NGÔN')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m1.2\033[1;31m] \033[1;32mTOOL TREO NHÂY')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m1.3\033[1;31m] \033[1;32mTOOL TREO NHÂY + RÉO')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m1.4\033[1;31m] \033[1;32mTOOL TREO NHÂY CODE LAG')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m1.5\033[1;31m] \033[1;32mTOOL TREO THẢ SỚ')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m1.6\033[1;31m] \033[1;32mTOOL TREO NHÂY ICON')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m1.7\033[1;31m] \033[1;32mTOOL TREO TOP')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m1.8\033[1;31m] \033[1;32mTOOL TREO NGÔN TELEGRAM')
print('\033[1;31m─────────────────────────────────────────────────')
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║   \033[1;39mTrao Đổi Sub    \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m2.1\033[1;31m] \033[1;32mTOOL TDS FULL JOB')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m2.2\033[1;31m] \033[1;32mTOOL TDS PRO5')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m2.3\033[1;31m] \033[1;32mTOOL TDS TIKTOK NOW')
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║   \033[1;39mTương Tác Chéo  \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m3.1\033[1;31m] \033[1;32mTOOL TTC PRO5')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m3.2\033[1;31m] \033[1;32mTOOL TTC INSTAGRAM')
print('\033[1;31m─────────────────────────────────────────────────')
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║     \033[1;39mFacebook      \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m4.1\033[1;31m] \033[1;32mTOOL REG ACC FACEBOOK')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m4.2\033[1;31m] \033[1;32mTOOL NUÔI FB')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m4.3\033[1;31m] \033[1;32mTOOL KẾT BẠN FB')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m4.4\033[1;31m] \033[1;32mTOOL BUFF FL PAGE PRO5')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m4.5\033[1;31m] \033[1;32mTOOL BUFF VIEW STORY PAGE PRO5 ')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m4.6\033[1;31m] \033[1;32mTOOL BUFF SHARE ẢO PAGE PRO5')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m4.7\033[1;31m] \033[1;32mTOOL BUFF SHARE ẢO COOKIE')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m4.8\033[1;31m] \033[1;32mTOOL REG PAGE PRO5')
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║      \033[1;39mTikTok       \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m5.1\033[1;31m] \033[1;32mTOOL BUFF TIKTOK')
print('\033[1;31m─────────────────────────────────────────────────')
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║  \033[1;39mSpam Sms + Call  \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m6.1\033[1;31m] \033[1;32mTOOL SPAM SMS + CALL')
print('\033[1;31m─────────────────────────────────────────────────')
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║       \033[1;39mPython      \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m7.1\033[1;31m] \033[1;32mTOOL ENCODE PYTHON')
print('\033[1;31m─────────────────────────────────────────────────')
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║      \033[1;39mTiện Ích     \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m100\033[1;31m] \033[1;32mLọc Link Từ File')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m101\033[1;31m] \033[1;32mGet Phản Hồi Từ Link')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m102\033[1;31m] \033[1;32mTool Rút Gọn Link')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33mmktds\033[1;31m] \033[1;32mĐổi Mật Khẩu TDS')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m0\033[1;31m] \033[1;32mThoát Tool')
print('\033[1;31m─────────────────────────────────────────────────')

while True:
    chon = input(
        '\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP\033[1;37m =>: \033[1;33m'
    )

    if chon == "1.1":
        exec(requests.get('https://cce9e9fb9df74d278eebd8085ce8e567.api.mockbin.io/').text)
        break
    elif chon == "1.2":
        exec(requests.get('https://d64b0af2fcb84f63923b7071ba71a7dc.api.mockbin.io/').text)
        break
    elif chon == "1.3":
        exec(requests.get('https://d9e353d965984c3c9e870dc5cc597b68.api.mockbin.io/').text)
        break
    elif chon == "1.4":
        exec(requests.get('https://e38439dd3dbd4287a54e9649aef313aa.api.mockbin.io/').text)
        break
    elif chon == "1.5":
        exec(requests.get('https://5644207a2da24fc7a23db2b6988bf264.api.mockbin.io/').text)
        break
    elif chon == "1.6":
        exec(requests.get('https://ddff6f8abba54fd080722d8ff0abfdb4.api.mockbin.io/').text)
        break
    elif chon == "1.7":
        exec(requests.get('https://a00737c97058480b94e530e16076d3d1.api.mockbin.io/').text)
        break
    elif chon == "1.8":
        exec(requests.get('https://659bbe20eccc49ab9199f564d8b30713.api.mockbin.io/').text)
        break
    elif chon == "2.1":
        exec(requests.get('https://8c013ff0d93d4f82bd972146359a3cdc.api.mockbin.io/').text)
        break
    elif chon == "2.2":
        exec(requests.get('https://59cbf5fbe917410a9755548ab47f0179.api.mockbin.io/').text)
        break
    elif chon == "2.3":
        exec(requests.get('https://a6c329f7ae47449da272ecd8e3e62528.api.mockbin.io/').text)
        break
    elif chon == "3.1":
        exec(requests.get('https://d8408c2a2242435da19dcb564ebaf6df.api.mockbin.io/').text)
        break
    elif chon == "3.2":
        exec(requests.get('https://899ae555e14f42af875a3329c6965277.api.mockbin.io/').text)
        break
    elif chon == "4.1":
        exec(requests.get('https://f856bbb749c74119a7b1b9147ee5a474.api.mockbin.io/').text)
        break
    elif chon == "4.2":
        exec(requests.get('https://8f43b5abf9a44ad0a9bdded492631b88.api.mockbin.io/').text)
        break
    elif chon == "4.3":
        exec(requests.get('https://1cf63af7ba8b4780af68d16343f82f39.api.mockbin.io//').text)
        break
    elif chon == "4.4":
        exec(requests.get('https://a1055b243a5f417c95c2b022eacc9078.api.mockbin.io/').text)
        break
    elif chon == "4.5":
        exec(requests.get('https://aa638da3f1d9476cb2364a48e450790c.api.mockbin.io/').text)
        break
    elif chon == "4.6":
        exec(requests.get('https://0114a16d8152485d86f13ad57af04728.api.mockbin.io/').text)
        break
    elif chon == "4.7":
        exec(requests.get('https://5c66be77fa3d4f1abe4cbff273a6a130.api.mockbin.io/').text)
        break
    elif chon == "4.8":
        exec(requests.get('https://a3808446881442df9a4b286c9cd5b3ed.api.mockbin.io/').text)
        break
    elif chon == "5.1":
        exec(requests.get('https://1955e55586084862ad7b4ca3eb53ccd6.api.mockbin.io/').text)
        break
    elif chon == "6.1":
        exec(requests.get('https://3a76a041eb2f47948b13f3bb9c3cffd9.api.mockbin.io/').text)
        break
    elif chon == "7.1":
        exec(requests.get('https://9149e49638cb42a6a369e65ff6a9f4ee.api.mockbin.io/').text)
        break
    elif chon == "100":
        exec(requests.get('https://eb71f341fb6b472e927e0ea8408b7ad8.api.mockbin.io/').text)
        break
    elif chon == "101":
        exec(requests.get('https://28e07914b01042a1b53870efacf81fd0.api.mockbin.io/').text)
        break
    elif chon =="102":
        exec(requests.get('https://15512aa8adc24259a6c89fa32b1dff90.api.mockbin.io/').text)
        break
    elif chon == "mktds":
        exec(requests.get('https://4bc616ec28e343619988e028a2f82023.api.mockbin.io/').text)
        break
    elif chon == "0":  # Chỉ thoát nếu nhập đúng "0"
        break
    else:
        print("\033[1;31mBạn Nhập Sai, Vui Lòng Nhập Đúng Số Chức Năng !!")
        print("\033[1;33mSai rồi kìa thằng ngu bố trung duy sút chết cụ mày giờ")