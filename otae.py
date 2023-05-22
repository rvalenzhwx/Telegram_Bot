#!/usr/bin/env python3

from telethon import TelegramClient
from telethon import functions, types

# Use your own values from my.telegram.org
api_id=22121264
api_hash='60d54a79b4c3accaf1994ac905b6f305'
bot_token='6089313919:AAEbUvfXa9nbNvQS1Puv1EKn1Td1NhhnHDQ'

## The first parameter is the .session file name (absolute paths allowed)
#with TelegramClient('anon', api_id, api_hash) as client:
#    client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))

with TelegramClient('pfarts', api_id, api_hash) as client:
    result = client(functions.messages.SendMessageRequest(
        peer='-1961359776',
        message='Hello there!',
        no_webpage=True,
        noforwards=True,
        update_stickersets_order=True,
        top_msg_id=42,
        schedule_date=datetime.datetime(2018, 6, 25),
        send_as='username'
    ))
    print(result.stringify())

