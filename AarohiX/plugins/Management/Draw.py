from pyrogram import filters
from pyrogram.types import  Message
from pyrogram.types import InputMediaPhoto
from AarohiX import app
from AarohiX import api
from pyrogram.enums import ChatAction,ParseMode

@app.on_message(filters.command("draw"))
async def draw_(b, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:

        text =message.text.split(None, 1)[1]
    nykaa=await message.reply_text( "🎨")
    try:
        await b.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        x=api.ai_image(text)
        with open("nykaa.jpg", 'wb') as f:
            f.write(x)
        caption = f"""Dʀᴀᴡɪɴɢ Iᴍᴀɢᴇ ʙʏ 𝐊꯭ʀ꯭ɪꜱ꯭꯭ʜ꯭"""
        await nykaa.delete()
        await message.reply_photo("nykaa.jpg",caption=caption,quote=True)
    except Exception as e:
        await nykaa.edit_text(f"⬤ ᴇʀʀᴏʀ ➥ {e}")
