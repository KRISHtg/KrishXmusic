import time
import random
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import config
from AarohiX import app
from AarohiX.misc import _boot_
from AarohiX.plugins.sudo.sudoers import sudoers_list
from AarohiX.utils import bot_sys_stats
from AarohiX.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from AarohiX.utils.decorators.language import LanguageStart
from AarohiX.utils.formatters import get_readable_time
from AarohiX.utils.inline import first_page, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string



YUMI_PICS = [
    "hhttps://te.legra.ph/file/dea69b6de713db64628d5.jpg",
    "https://te.legra.ph/file/cbdc7b55600c7f7c982be.jpg",
    "https://graph.org/file/f76fd86d1936d45a63c64.jpg",
    "https://te.legra.ph/file/799211ecd1dfb26d70ea0.jpg",
    "https://te.legra.ph/file/6d585197af34afd4bb740.jpg",
    "https://te.legra.ph/file/8020cf0424c438f36dafb.jpg",
    "https://te.legra.ph/file/88d38fe8a1d4560a3b6e5.jpg",
    "https://te.legra.ph/file/501a638b8917f978e7e1d.jpg",
    "https://te.legra.ph/file/67b3cbaa39ca5b8c68633.jpg",
    "https://te.legra.ph/file/31b8d89e7bde2b1b53871.jpg"
]

STICKERS = [
    "CAACAgUAAx0Cd6nKUAACASBl_rnalOle6g7qS-ry-aZ1ZpVEnwACgg8AAizLEFfI5wfykoCR4h4E",
    "CAACAgUAAx0CfL_LsAACCSRl_oru7uW8WAt3-L1pYQWe_1mxawACQw8AAj78MVeb3v2OFvEnNB4E",
    "CAACAgEAAx0Cd6nKUAACATVl_rtAi9KCVQf8vcUC4FMDUfLP8wACHQEAAlEpDTnhphyRDaTrPR4E",
    "CAACAgUAAx0Cd6nKUAACATJl_rsEJOsaaPSYGhU7bo7iEwL8AAPMDgACu2PYV8Vb8aT4_HUPHgQ",

]

async def delete_sticker_after_delay(message, delay):
    await asyncio.sleep(delay)
    await message.delete()

@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = first_page(_)
            sticker_message = await message.reply_sticker(sticker=random.choice(STICKERS))
            asyncio.create_task(delete_sticker_after_delay(sticker_message, 2))  # Delete sticker after 2 seconds
            return await message.reply_photo(
                await message.reply_photo(
                random.choice(ANNIE),
                caption=_["help_1"].format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
            )
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
            )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("**» sᴇᴀʀᴄʜɪɴɢ ʙᴀʙʏ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = _["start_6"].format(
                title, duration, views, published, channellink, channel, app.mention
            )
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=_["S_B_8"], url=link),
                        InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_CHAT),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                chat_id=message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                reply_markup=key,
            )
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
    else:
        out = private_panel(_)
        sticker_message = await message.reply_sticker(sticker=random.choice(STICKERS))
        asyncio.create_task(delete_sticker_after_delay(sticker_message, 2))  # Delete sticker after 2 seconds
        await message.reply_photo(
            await message.reply_photo(
                random.choice(ANNIE),,
            caption=_["start_2"].format(message.from_user.mention, app.mention),
            reply_markup=InlineKeyboardMarkup(out),
        )
        if await is_on_off(2):
            return await app.send_message(
                chat_id=config.LOGGER_ID,
                text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
            )

@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_photo(
                random.choice(ANNIE),,
        caption=_["start_1"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
    )
    return await add_served_chat(message.chat.id)

@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass
            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)
                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)
                await message.reply_photo(
                random.choice(ANNIE),,
                    caption=_["start_3"].format(
                        message.from_user.mention,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)


                                
