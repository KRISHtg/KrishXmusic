from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ANNIEMUSIC import app
from config import BOT_USERNAME

start_txt = """**
✪ ωεℓ¢σмє ƒσя jคяv¡ร яєρσѕ ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
     
            [ 
            InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴀʙᴇs✪", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
     
            [
             InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/queen_suportgroup"),
             InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/Queen_update"),
             ],
     
             [
             InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/queen_suportgroup"),          
             InlineKeyboardButton("︎ᴍᴜsɪᴄ", url=f"https://github.com/KRISHtg/queenmusicbot"),
             ],
     
              ]
 
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/9e6ad9d95b0a61baf5dd1.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
