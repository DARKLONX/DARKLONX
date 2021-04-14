# COPYRIGHT (C) 2021 BY DARKLONX
"""
(((((((((((((((((((((((@DARKLONX)))))))))))))))))))))))))))
(((((((((((((((((((((((@DARKLONX)))))))))))))))))))))))))))
(((((((((((((((((((((((@DARKLONX)))))))))))))))))))))))))))
(((((((((((((((((((((((@DARKLONX)))))))))))))))))))))))))))
"""
# MADE BY DARKLONX 🔥
# MY IDEA H YRR DONT KANG THIS PLEASE
import asyncio
import os
try:
  from pyrogram import Client, idle
except:
  os.system("pip install pyrogram>=1.1.13")
  from pyrogram import Client, idle

import asyncio
from DARKLONX.utils import admin_cmd as legendx
from DARKLONX import bot as DARKLONX
API_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
from telethon import events, custom, Button, TelegramClient
import time
from DARKLONX import botnickname, ALIVE_NAME, bot
token = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
xbot = TelegramClient("legend", API_ID, API_HASH).start(bot_token=token)
pbot = Client("DARKLONX", api_id=API_ID, api_hash=API_HASH, bot_token=token)
BOT = str(botnickname) if botnickname else "DARKLONX BOT"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "DARKLONX BOY"
PHOTO = os.environ.get("ALIVE_PHOTTO", None)
DARKLONX = "[DARKLONX X](https://t.me/DARKLONX)"
VERSION = "3.1.5"
ID = 1100231654
REPO = "[DARKLONX BOT](https://github.com/DARKLONX/DARKLONX)"
PRO = bot.uid
MASTER = f"[{NAME}](tg://user?id={PRO})"
GROUP = "[SUPPORT GROUP](https://t.me/DARKLONX_USERBOT_SUPPORT)"
if __name__=="__main__":
  xbot.run_until_disconnected()

if __name__=="__main__":
  pbot.start()
  run()
