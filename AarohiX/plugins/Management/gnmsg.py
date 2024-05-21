import re
from pyrogram import filters
import random
from AarohiX import app


@app.on_message(filters.command(["gn","n","oodnight","ood Night","ood night"], prefixes=["/","g","G"]))
def goodnight_command_handler(_, message):
    sender = message.from_user.mention
    send_sticker = random.choice([True, False])
    if send_sticker:
        sticker_id = get_random_sticker()
        app.send_sticker(message.chat.id, sticker_id)
        message.reply_text(f"**❀ ᴡɪsʜɪɴɢ ʏᴏᴜ ᴀ ᴠᴇʀʏ ɢᴏᴏᴅ ɴɪɢʜᴛ ❀.\n\n✦ ᴍᴀʏ ᴛʜᴇ ᴀɴɢᴇʟs ғʀᴏᴍ ʜᴇᴀᴠᴇɴ ʙʀɪɴɢ ᴛʜᴇ sᴡᴇᴇᴛᴇsᴛ ᴏғ ᴀʟʟ ᴅʀᴇᴀᴍs ғᴏʀ ʏᴏᴜ. ᴍᴀʏ ʏᴏᴜ ʜᴀᴠᴇ ʟᴏɴɢ ᴀɴᴅ ʙʟɪssғᴜʟ sʟᴇᴇᴘ ғᴜʟʟ ᴏғ ʜᴀᴘᴘʏ ᴅʀᴇᴀᴍs\n\n✦ ᴡɪsʜɪɴɢ ᴛᴏ ➛ {sender}!\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ 𝐊𝐑𝐈𝐒𝐇 🌙**")
    else:
        emoji = get_random_emoji()
        app.send_message(message.chat.id, emoji)
        message.reply_text(f"**❀ ᴡɪsʜɪɴɢ ʏᴏᴜ ᴀ ᴠᴇʀʏ ɢᴏᴏᴅ ɴɪɢʜᴛ ❀.\n\n✦ ᴍᴀʏ ᴛʜᴇ ᴀɴɢᴇʟs ғʀᴏᴍ ʜᴇᴀᴠᴇɴ ʙʀɪɴɢ ᴛʜᴇ sᴡᴇᴇᴛᴇsᴛ ᴏғ ᴀʟʟ ᴅʀᴇᴀᴍs ғᴏʀ ʏᴏᴜ. ᴍᴀʏ ʏᴏᴜ ʜᴀᴠᴇ ʟᴏɴɢ ᴀɴᴅ ʙʟɪssғᴜʟ sʟᴇᴇᴘ ғᴜʟʟ ᴏғ ʜᴀᴘᴘʏ ᴅʀᴇᴀᴍs.\n\n✦ ᴡɪsʜɪɴɢ ᴛᴏ ➛ {sender}!\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ 𝐊𝐑𝐈𝐒𝐇 {emoji}**")


def get_random_sticker():
    stickers = [
        "CAACAgEAAxkBAAI3QWZAbTDUuSyYuBFEICpE5MEFg15qAALtAANRKQ05Nle8l0hfCh81BA", 
        "CAACAgUAAxkBAAI3RGZAbUn-aH5kx_LBHU_oRPGws1GCAALWCgACJBnRVrMPPAABZo3w3TUE", 
        "CAACAgUAAxkBAAI3R2ZAbbvD8Wp_alrtTKbZ7uCdMhO6AAI4CQACipHZVgOPIro46v8_NQQ", 
        "CAACAgQAAxkBAAI3SmZAbdp2ujUSMHQCJGxTQP8GESxpAAKGCwACNEtYU07VH1KATRO5NQQ",
        "CAACAgUAAxkBAAI3UGZAbgUDhI3rTVuhLzSTz7SPnjYOAAJrBAACvpHQVeX-xU2uamVsNQQ",
    ]
    return random.choice(stickers)


def get_random_emoji():
    emojis = [
        "😴",
        "💤",
    ]
    return random.choice(emojis)
    
