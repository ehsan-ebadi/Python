
#---------------------------  Path  ---------------------------
https://docs.python.org/3/library/index.html

#---------------------------  Types  ---------------------------
Core > int, type
Built-in > print, len
Import > math, random

#---------------------------  Usage  ---------------------------
import random
random.randint(1, 10) 

from random import randint
randint(1, 10)

import datetime
datetime.date.today()
#datetime.date(2020, 7, 8)
datetime.datetime.now().strftime(“%Y%m%d”)
#'20200708'

import sys
sys.platform
#‘win32’
sys.getwindowsversion()
#sys.getwindowsversion(major=6, minor=2, build=9200, platform=2, service_pack=’’)

import os
os.listdir(“c:”)
os.stat(“test.txt”)
os.system(“cmd.exe”)

import ctypes
libc = ctypes.CDLL(“test.dll”)
counter = libc.simple_function()

pip install pynput

import pynput
def process_key_press(key):
    print(key)
keyboard_listener = pynput.keyboard.Listener(on_press = process_key_press)
with keyboard_listener:
    keyboard_listener.join()

#---------------------------  PIP  ---------------------------
python -m ensurepip --default-pip

pip3:
# echo ""deb http://http.kali.org/kali kali-rolling main non-free contrib"" | sudo tee /etc/apt/sources.list
# apt update && apt upgrade 
# apt install python3-pip 
or
# Download ==> https://bootstrap.pypa.io/get-pip.py
# python3 get-pip.py"

# Path >  C:\Users\ehsan\AppData\Local\Programs\Python\Python38-32\Scripts
# Must Add to Environment Virable

pip install jdatetime
# python
import jdatetime
