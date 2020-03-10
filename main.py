import requests
import json
import datetime
import random
import string
import os
import time 

referrer = str()
while len(referrer) != 36:
    referrer = input("USER ID (Setting/More settings/Diagnostics/ID): ")

def genString(stringLength):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))

ver = 'v0a745'
url = f'https://api.cloudflareclient.com/{ver}/reg'

def run():
    install_id = genString(13)
    body = {"key": "{}=".format(genString(42)),
            "install_id": install_id,
            "fcm_token": f"{install_id}:APA91b{genString(134)}",
            "referrer": referrer,
            "warp_enabled": False,
            "tos": datetime.datetime.now().isoformat()[:-3] + "+07:00",
            "type": "Android",
            "locale": "zh-CN"}

    bodyString = json.dumps(body)

    headers = {'Content-Type': 'application/json; charset=UTF-8',
               'Host': 'api.cloudflareclient.com',
               'Connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip',
               'User-Agent': 'okhttp/3.12.1'
               }

    r = requests.post(url, data=bodyString, headers=headers)
    return r
    

if __name__ == "__main__":
    while True:
        result = run()
        if result.status_code == 200:
            print("+1 GB")
            time.sleep(15)