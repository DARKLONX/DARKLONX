# COPYRIGHT (C) 2021 BY LEGENDX AND PROBOYX, ALAIN

"""
(((((((((((((((((((((((@LEGENDX)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX)))))))))))))))))))))))))))
                 MADE BY LEGENDX AND PROBOY X
                   DISIGNED BY ALAIN_CHAMPION
                   CREDITS #TEAMLEGENDX 
                PLEASE DON'T REMOVE THIS LINES
"""

from telethon import events, Button, custom
import re, os
from LEGENDX import Photo, xbot, VERSION
from LEGENDX import bot
@xbot.on(events.NewMessage(pattern=("/alive|/start")))
async def awake(event):
  LEGENDX = f"ʜᴇʟʟᴏ ᴛʜɪs ɪs  {BOT}\n\n"
  LEGENDX += "ᴀʟʟ sʏsᴛᴇᴍ ɪs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ\n\n"
  LEGENDX += f"{BOT} VERSION : {VERSION} ʟᴀsᴛᴇsᴛ\n\n"
  LEGENDX += f"ᴍʏ ᴍᴀsᴛᴇʀ @{bot.me.username} ☺️\n\n"
  LEGENDX += "ғᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ\n\n"
  LEGENDX += "ᴛᴇʟᴇᴛʜᴏɴ : 1.20 LATEST\n\n"
  LEGENDX += "ᴛʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ"
  BUTTON = [[Button.url("𝙼𝙰𝚂𝚃𝙴𝚁", f"https://t.me/{bot.me.username}"), Button.url(f"{BOT} 𝚁𝙴𝙿𝙾", "https://github.com/LEGENDX/LEGENDX")]]
  BUTTON += [[custom.Button.inline("𝚁𝙴𝙿𝙾𝚂𝙸𝚃𝙾𝚁𝚈", data="LEGENDX")]]
  await xbot.send_file(event.chat_id, PHOTO, caption=LEGENDX,  buttons=BUTTON)




@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"LEGENDX")))
async def callback_query_handler(event):
# inline by LEGENDX and PROBOY22 🔥
  PROBOYX = [[Button.url("REPO-LEGENDX", "https://github.com/LEGENDX/LEGENDXX")]]
  PROBOYX +=[[Button.url("DEPLOY-LEGENDX", )]]
  PROBOYX +=[[Button.url("TUTORIAL", ""), Button.url("STRING-SESSION", "https://repl.it/@LEGENDX22/LEGEND-Bot#main.py")]]
  PROBOYX +=[[Button.url("API_ID & HASH", "https://t.me/usetgxbot"), Button.url("REDIS", "https://redislabs.com")]]
  PROBOYX +=[[Button.url("SUPPORT CHANNEL", "https://t.me/LEGENDXCHAT"), Button.url("SUPPORT GROUP", "https://t.me/LEGENDXCHAT")]]
  PROBOYX +=[[custom.Button.inline("ALIVE", data="PROBOY")]]
  await event.edit(text=f"𝙰𝙻𝙻 𝙳𝙴𝚃𝙰𝙸𝙻𝚂 𝙾𝙵 𝚁𝙴𝙿𝙾𝚂", buttons=PROBOYX)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"LEGENDX")))
async def callback_query_handler(event):
# inline by LEGENDX and PROBOY22 🔥
  LEGENDX = f"ʜᴇʟʟᴏ ᴛʜɪs ɪs  {BOT}\n\n"
  LEGENDX += "ᴀʟʟ sʏsᴛᴇᴍ ɪs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ\n\n"
  LEGENDX += f"{BOT} OS : {VERSION} ʟᴀsᴛᴇsᴛ\n\n"
  LEGENDX += f"ᴍʏ ᴍᴀsᴛᴇʀ @{bot.me.username} ☺️\n\n"
  LEGENDX += "ғᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ\n\n"
  LEGENDX += "ᴛᴇʟᴇᴛʜᴏɴ : 1.20 LATEST\n\n"
  LEGENDX += "ᴛʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ"
  BUTTONS = [[Button.url("𝙼𝙰𝚂𝚃𝙴𝚁", f"https://t.me/{bot.me.username}"), Button.url(f"{BOT} 𝚁𝙴𝙿𝙾", "https://github.com/LEGENDX/LEGENDX")]]
  BUTTONS += [[custom.Button.inline("𝚁𝙴𝙿𝙾𝚂𝙸𝚃𝙾𝚁𝚈", data="LEGENDX")]]
  await event.edit(text=LEGENDX, buttons=BUTTONS)


@xbot.on(events.NewMessage(pattern=("/repo|#repo")))
async def repo(event):
  await xbot.send_message(event.chat, "ʀᴇᴘᴏ ᴏғ ʟᴇɢᴇɴᴅ-ʙᴏᴛ", buttons=[[Button.url("⚜️ ʀᴇᴘᴏ ⚜️", "https://github.com/LEGENDX/LEGENDX")]])
