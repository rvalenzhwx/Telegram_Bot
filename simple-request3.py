#!/usr/bin/env python3

import requests
url="https://api.telegram.org/bot6089313919:AAFSDSBPeLN_Q85EyV5KVyIPEYQBzUvRwAI/sendMessage"

payload = {
    'chat_id' : '-1001961359776', 'text': 'Pal Andres'
}
retval=requests.get(url, params=payload)
