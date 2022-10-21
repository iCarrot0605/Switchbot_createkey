#!/usr/bin/env python3

import time
import hashlib
import hmac
import base64
import json
import uuid
import requests

def gensign(token, secret):
    nonce = str(uuid.uuid4())
    t = int(round(time.time() * 1000))
    string_to_sign = '{}{}{}'.format(token, t, nonce)

    string_to_sign = bytes(string_to_sign, 'utf-8')
    secret = bytes(secret, 'utf-8')

    sign = base64.b64encode(hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())

    header={}
    header["Authorization"] = token
    header["sign"] = str(sign, 'utf-8')
    header["t"] = str(t)
    header["nonce"] = nonce

    return header

body = {
    "commandType": "command",
    "command": "createKey",
    "parameter": {
        "name": "Guest Code",
        "type": "timeLimit",
        "password": "135792468",
        "startTime": 1664640056,
        "endTime": 1665331432
    }
}

token = ''
secret = ''
deviceId = ''

header = gensign(token, secret)

result = requests.post("https://api.switch-bot.com/v1.1/devices/" + deviceId + "/commands", headers=header, data=json.dumps(body))
print(json.loads(result.text))
