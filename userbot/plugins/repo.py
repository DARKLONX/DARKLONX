# COPYRIGHT © BY LEGENDX

"""
(((((((((((((((((((((((@LEGENDX)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX)))))))))))))))))))))))))))

                 MADE BY LEGENDX
                 IDEA BY PROBOYX
                 CREDITS TEAMLEGENDX
                 PLEASE KEEP CREDITS 🥺
"""



from telethon import events, Button, custom
from LEGENDX import BOT
import os,re
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
@tgbot.on(events.InlineQuery(pattern=r"repo"))
async def inline_id_handler(event: events.InlineQuery.Event):
 LEGENDX = event.builder
 X= [[custom.Button.inline("🔥 CLICK ME 🔥",data="obhai")]]
 query = event.text
 result = LEGENDX.article("LEGENDX",text="REPO AND SUPPORT",buttons=X,link_preview=False)
 await event.answer([result])
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"obhai")))
async def callback_query_handler(event):

# inline by LEGENDX and PROBOYX 🔥
  await event.edit(text=f"{BOT} REPO AND GROUP LINK",buttons=[[Button.url(f"🔥{BOT} REPO🔥", url="https://github.com/LEGENDX/LEGENDX"), Button.url(f"⚡{BOT} SUPPORT⚡", url="https://t.me/LEGENDX_USERBOT_SUPPORT")]])
