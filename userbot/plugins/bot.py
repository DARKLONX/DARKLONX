# make by @DARKLONX22
# inline alive
# modify by proboy22
import asyncio
import os
from DARKLONX import BOT, PHOTO, VERSION
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from userbot import bot as borg
from telethon.tl.custom import Button
from telethon.tl.types import ChannelParticipantsAdmins
global ok
ok = borg.uid
from userbot.utils import admin_cmd
from PIL import Image
import requests
from io import BytesIO
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DARKLONX BOY"
ALIVE_PHOTTO = PHOTO

pro_text=(f"**{BOT} IS ON FIRE **\n\n**Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...**\n\n🔥 About My System 🔥\n\n➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ 1.20\n➾ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** ☞ [ᴊᴏɪɴ](https://t.me/DARKLONXBOT_OFFICIAL)\n➾ **ʟɪᴄᴇɴꜱᴇ**  ☞ [DARKLONX BOT](https://github.com/DARKLONX)\n➾ **ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ** ☞ [DARKLONX](https://github.com/DARKLONX/DARKLONX)\n\n➾ **ᴍʏ ᴍᴀsᴛᴇʀ** ☞ [{DEFAULTUSER}](tg://user?id={ok})\n")
TG_BOT_USER_NAME_BF_HER = os.environ.get("ALIVE_PHOTTO", None)
if TG_BOT_USER_NAME_BF_HER is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        me = await borg.get_me()
        if query.startswith("alive") and event.query.user_id == me.id:
            buttons = [
                [
                    Button.url("Repo", "https://github.com/DARKLONXOP/DARKLONX"),
                    Button.url("Deploy", "https://heroku.com/deploy?template=https://github.com/DARKLONX/DARKLONX/blob/master")],
                    [Button.url("String", "https://repl.it/DARKLONX/DARKLONX#main.py"),
                    Button.url("Channel", "https://t.me/teamishere"),
                ]
            ]
            if ALIVE_PHOTTO and ALIVE_PHOTTO.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    ALIVE_PHOTTO,
                    text=pro_text,
                    buttons=buttons,
                    link_preview=False
                )
            elif ALIVE_PHOTTO:
                result = builder.document(
                    ALIVE_PHOTTO,
                    title="DARKLONX BOT",
                    text=pro_text,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="DARKLONX BOT",
                    text=pro_text,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)



from userbot import bot


@bot.on(admin_cmd(outgoing=True, pattern="alive"))
async def repo(event):
    if event.fwd_from:
        return
    DARKLONX = Var.TG_BOT_USER_NAME_BF_HER
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(DARKLONX, "alive")
    await response[0].click(event.chat_id)
    await event.delete()
