# COPYRIGHT © BY DARKLONX

"""
(((((((((((((((((((((((@DARKLONX)))))))))))))))))))))))))))
(((((((((((((((((((((((@DARKLONX)))))))))))))))))))))))))))
(((((((((((((((((((((((@DARKLONX)))))))))))))))))))))))))))
(((((((((((((((((((((((@DARKLONX)))))))))))))))))))))))))))

                 MADE BY DARKLONX
                 IDEA BY PROBOYX
                 CREDITS TEAMDARKLONX
                 PLEASE KEEP CREDITS 🥺
"""



from telethon import events, Button, custom
from DARKLONX import BOT
import os,re
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
@tgbot.on(events.InlineQuery(pattern=r"repo"))
async def inline_id_handler(event: events.InlineQuery.Event):
 DARKLONX = event.builder
 X= [[custom.Button.inline("🔥 CLICK ME 🔥",data="obhai")]]
 query = event.text
 result = DARKLONX.article("DARKLONX",text="REPO AND SUPPORT",buttons=X,link_preview=False)
 await event.answer([result])
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"obhai")))
async def callback_query_handler(event):

# inline by DARKLONX and PROBOYX 🔥
  await event.edit(text=f"{BOT} REPO AND GROUP LINK",buttons=[[Button.url(f"🔥{BOT} REPO🔥", url="https://github.com/DARKLONX/DARKLONX"), Button.url(f"⚡{BOT} SUPPORT⚡", url="https://t.me/DARKLONX_USERBOT_SUPPORT")]])
