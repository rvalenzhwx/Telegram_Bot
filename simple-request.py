#!/usr/bin/env python3

import requests
import json
import os
from dotenv import load_dotenv





url="https://api.telegram.org/bot6089313919:AAFSDSBPeLN_Q85EyV5KVyIPEYQBzUvRwAI/sendMessage"
#url = "https://api.telegram.org/bot6089313919:AAEbUvfXa9nbNvQS1Puv1EKn1Td1NhhnHDQ/getMe"

config = dotenv_values(".env")
print(config)



payload = {
    'chat_id' : '-1001961359776', 'text': 'Text TEST'
}


#headers = {
#    "accept": "application/json",
#    "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
#    "content-type": "application/json"
#}

#response = requests.post(url, json=payload, headers=headers)
#response=requests.post(url)
retval=requests.get(url, params=payload)
jsondec=.json()
strs=str(jsondec)
print(retval.url)
print(retval.text)
print(jsondec)
