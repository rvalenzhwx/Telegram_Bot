#!/usr/bin/env python3

import requests
import os
from dotenv import load_dotenv

load_dotenv()
key1='URL'

payload = {
    'chat_id' : '-1001961359776', 'text': 'Pal Andres'
}

retval=requests.get(os.getenv(key1), params=payload)
print(retval.url)
print(retval.text)
