import re
from pyrogram import filters
import random
from AarohiX import app


@app.on_message(filters.command(["gm","m","oodmorning","ood Morning","ood morning"], prefixes=["/","g","G"]))
def goodnight_command_handler(_, message):
    sender = message.from_user.mention
    send_sticker = random.choice([True, False])
    if send_sticker:
        sticker_id = get_random_sticker()
        app.send_sticker(message.chat.id, sticker_id)
        message.reply_text(f"**❀ᴡɪsʜɪɴɢ ʏᴏᴜ ᴀ ᴠᴇʀʏ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ❀.\n\n● ᴡᴇʟᴄᴏᴍᴇ ᴛʜɪs ʙᴇᴀᴜᴛɪғᴜʟ ᴍᴏʀɴɪɴɢ ᴡɪᴛʜ ᴀ sᴍɪʟᴇ ᴏɴ ʏᴏᴜʀ ғᴀᴄᴇ. I ʜᴏᴘᴇ ʏᴏᴜ ʟʟ ʜᴀᴠᴇ ᴀ ɢʀᴇᴀᴛ ᴅᴀʏ ᴛᴏᴅᴀʏ.\n\n✦ ᴡɪsʜɪɴɢ ᴛᴏ ➛ {sender}!\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ 𝐊𝐑𝐈𝐒𝐇 🌙**")
    else:
        emoji = get_random_emoji()
        app.send_message(message.chat.id, emoji)
        message.reply_text(f"**❀ᴡɪsʜɪɴɢ ʏᴏᴜ ᴀ ᴠᴇʀʏ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ❀.\n\n● ᴡᴇʟᴄᴏᴍᴇ ᴛʜɪs ʙᴇᴀᴜᴛɪғᴜʟ ᴍᴏʀɴɪɴɢ ᴡɪᴛʜ ᴀ sᴍɪʟᴇ ᴏɴ ʏᴏᴜʀ ғᴀᴄᴇ. I ʜᴏᴘᴇ ʏᴏᴜ ʟʟ ʜᴀᴠᴇ ᴀ ɢʀᴇᴀᴛ ᴅᴀʏ ᴛᴏᴅᴀʏ..\n\n✦ ᴡɪsʜɪɴɢ ᴛᴏ ➛ {sender}!\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ 𝐊𝐑𝐈𝐒𝐇 {emoji}**")


def get_random_sticker():
    stickers = [
        "CAACAgUAAxkBAAI4smZOnxEc8HdScAQAAdI0d_v8QmPEfwACOAkAAoqR2VYDjyK6OOr_PzUE", 
        "CAACAgUAAxkBAAI4tWZOn5Pb3qnWhp5FA90lLBklIvEZAALGDgACthSQVOqJjVEZWDRRNQQ",
    ]
    return random.choice(stickers)


def get_random_emoji():
    emojis = [
        "☀️",
        "🌥️",
    ]
    return random.choice(emojis)
    
