import re
from pyrogram import filters
import random
from AarohiX import app


@app.on_message(filters.command(["gm","m","oodmorning","ood Morning","ood morning"], prefixes=["/","g","G"]))
def goodnight_command_handler(_, message):
    sender = message.from_user.mention
        message.reply_text(f"**❀ᴡɪsʜɪɴɢ ʏᴏᴜ ᴀ ᴠᴇʀʏ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ❀.\n\n● ᴡᴇʟᴄᴏᴍᴇ ᴛʜɪs ʙᴇᴀᴜᴛɪғᴜʟ ᴍᴏʀɴɪɴɢ ᴡɪᴛʜ ᴀ sᴍɪʟᴇ ᴏɴ ʏᴏᴜʀ ғᴀᴄᴇ. I ʜᴏᴘᴇ ʏᴏᴜ ʟʟ ʜᴀᴠᴇ ᴀ ɢʀᴇᴀᴛ ᴅᴀʏ ᴛᴏᴅᴀʏ.\n\n✦ ᴡɪsʜɪɴɢ ᴛᴏ ➛ {sender}!\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ 𝐐ᴜᴇᴇɴ ✘ 𝐌ᴜꜱɪᴄ 🌙**")
else:
        message.reply_text(f"**❀ᴡɪsʜɪɴɢ ʏᴏᴜ ᴀ ᴠᴇʀʏ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ❀.\n\n● ᴡᴇʟᴄᴏᴍᴇ ᴛʜɪs ʙᴇᴀᴜᴛɪғᴜʟ ᴍᴏʀɴɪɴɢ ᴡɪᴛʜ ᴀ sᴍɪʟᴇ ᴏɴ ʏᴏᴜʀ ғᴀᴄᴇ. I ʜᴏᴘᴇ ʏᴏᴜ ʟʟ ʜᴀᴠᴇ ᴀ ɢʀᴇᴀᴛ ᴅᴀʏ ᴛᴏᴅᴀʏ..\n\n✦ ᴡɪsʜɪɴɢ ᴛᴏ ➛ {sender}!\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ 𝐐ᴜᴇᴇɴ ✘ 𝐌ᴜꜱɪᴄ {emoji}**")


