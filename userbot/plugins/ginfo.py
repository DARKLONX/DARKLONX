"""
(((((((((((((((((((((((@DARKLONX)))))))))))))))))))))))))))
(((((((((((((((((((((((@DARKLONX)))))))))))))))))))))))))))
(((((((((((((((((((((((@DARKLONX)))))))))))))))))))))))))))
(((((((((((((((((((((((@DARKLONX)))))))))))))))))))))))))))


                  made by @DARKLONX
                  credits TEAMDARKLONX
                  idea by @Alain_Champion 
 ((((((((((((((((((((((((( @DARKLONX AND @PROBOYX)))))))))))))))))))))))))))
"""
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP
from userbot.utils import admin_cmd
from DARKLONX import MASTER
DARKLONX = MASTER
PROBOY = "@tgscanrobot"
# MADE BY DARKLONX 🔥🔥

@borg.on(admin_cmd("ginfo ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    DARKLONX = event.pattern_match.group(1)
    if "@" in DARKLONX:
        async with borg.conversation(PROBOY) as conv:
            try:
                
                await event.edit(f"THIS USER DETAILS CHECKING BY {DARKLONX}")
                await conv.send_message("/start")
                await conv.get_response() #made by DARKLONX
                await conv.send_message(f"{DARKLONX}")
                TEAMX = await conv.get_response()
                await borg.send_message(event.chat_id, TEAMX.text)
                await event.delete() #made by DARKLONX
            except YouBlockedUserError:
                await event.edit("Error: @tgscanrobot unblock and retry!")
    elif DARKLONX == "":
        OP = await event.get_reply_message()
        PRO = OP.sender.id 
        async with borg.conversation(PROBOY) as conv:
            try: #made by DARKLONX 🔥
              #made by DARKLONX 
                await event.edit(f"THIS USER DETAILS CHECKING BY {DARKLONX}")
                await conv.send_message("/start")
                await conv.get_response() #made by DARKLONX
                await conv.send_message(f"{PRO}")
                TEAMX = await conv.get_response()
                await borg.send_message(event.chat_id, TEAMX.text)
                await event.delete()
            except YouBlockedUserError: #made by DARKLONX
                await event.edit("Error: unblock @tgscanrobot and try again!")
    else:
        async with borg.conversation(PROBOY) as conv:
            try: #made by DARKLONX 🔥
                
                await event.edit(f"THIS USER DETAILS CHECKING BY {DARKLONX}") 
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message(f"{PRO}")
                TEAMX = await conv.get_response()
                await borg.send_message(event.chat_id, TEAMX.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: unblock  @tgscanrobot `and try again!")
CMD_HELP.update({
    "ginfo ":"type .ginfo <@username> or tag a user type .ginfo 🔥"})
