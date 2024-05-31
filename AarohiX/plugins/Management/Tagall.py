from asyncio import sleep
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from ... import app, SUDO_USER, spam_chats
from ... import *

def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

@app.on_message(
    filters.command(["all", "utag" , "mention", "mentionall"], prefixes=["/", "@", ".", "#"])
    & admin_filter
)
    chat_id = message.chat.id
    direp = message.reply_to_message
    args = get_arg(message)
    if not direp and not args:
        return await message.edit("** ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ, ʟɪᴋᴇ »** `@utag Hi Friends`")
    await message.delete()
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}), "
        if usrnum == 4:
            if args:
                txt = f"{args}\n\n{usrtxt}"
                await client.send_message(chat_id, txt)
            elif direp:
                await direp.reply(usrtxt)
            await sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_message(
    filters.command(
        ["stoputag", "stopall", "offall", "offutag", "utagoff", "cancel"],
        prefixes=["/", ".", "@", "#"],
    )
    & admin_filter
)
    if not message.chat.id in spam_chats:
        return await message.edit("**It seems there is no tagall here.**")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.edit("**Cancelled.**")


__NAME__ = "Tᴀɢᴀʟʟ"
__MENU__ = """
`.utag` - **.utag (message) - to start usertagger**
`.cancel` - **to stop tagger**
`.tagall` - **.tagall - to start tagall**
`.tagallstop` - **to stop tagger**
`.vctag` - **voice msg tagall**
`.vctagstop` - **to stop tagger**
.gntag` - **good night msg tagall**
`.gntop` - **to stop tagger**
`.gmtag` - **good morning tagall**
`.gmstop` - **to stop tagger**
`.shayari` - **good night msg tagall**
`.shayaristop` - **to stop tagger**

"""
