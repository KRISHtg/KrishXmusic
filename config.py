import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env file
load_dotenv()

# Telegram API credentials - Get these from the Telegram API website
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

# Specify where to get the following credentials
OWNER_USERNAME = getenv("OWNER_USERNAME", "Its_krish_tg")
BOT_USERNAME = getenv("BOT_USERNAME", "Queen_of_heart_music_bot")
BOT_NAME = getenv("BOT_NAME", "𝐐ᴜᴇᴇɴ ✘ 𝐌ᴜꜱɪᴄ")
ASSUSERNAME = getenv("ASSUSERNAME", "Snowfall_xc")
EVALOP = list(map(int, getenv("EVALOP", "6745609407").split()))
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
LOGGER_ID = int(getenv("LOGGER_ID", -1001921995918))
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# External APIs - Get these from their respective providers
GPT_API = getenv("GPT_API")
DEEP_API = getenv("DEEP_API")
OWNER_ID = int(getenv("OWNER_ID", 6745609407))

# Heroku deployment settings - Refer to Heroku documentation on how to obtain these
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/KRISHtg/queenmusicbot")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Support and contact information - Provide your own support channels
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Queen_update")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Queen_update")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")

# Server limits and configurations - These can be set based on your server configurations
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "2500"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

# External service credentials - Obtain these from Spotify
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")

# Telegram file size limits - Set these according to your requirements
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

# Pyrogram session strings - You need to generate these yourself
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# Bot introduction messages - These can be customized as per your preference
AYU = [
    "💞", "🦋", "🔍", "🧪", "🦋", "⚡️", "🔥", "🦋", "🎩", "🌈", "🍷", "🥂", "🦋", "🥃", "🥤", "🕊️",
    "🦋", "🦋", "🕊️", "🦋", "🕊️", "🦋", "🦋", "🦋", "🪄", "💌", "🦋", "🦋", "🧨"
]

AYUV = [
    "❖ нᴇʏ</b> {0}, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ !</b>\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n<b>● ʜᴇʏ, ɪ ᴀᴍ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ꜱᴜᴘᴇʀꜰᴀꜱᴛ ᴍᴜꜱɪᴄ ʙᴏᴛ</b>\n\n<b>● ꜰᴇᴇʟ ꜰʀᴇᴇ ᴛᴏ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ, ᴀɴᴅ ᴇɴᴊᴏʏ... ɴᴏ ʟᴀɢ ᴀᴜᴅɪᴏ ᴀɴᴅ ᴠɪᴅᴇᴏ\n<b>● ᴢᴇʀᴏ ᴅᴏᴡɴᴛɪᴍᴇ ᴀɴᴅ ʟᴀɢ ꜰʀᴇᴇ ᴍᴜꜱɪᴄ 🎶\n\n<b>❖ ᴛʜɪs ɪs ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ʙᴏᴛ, ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴠᴄ.</b>\n\nʙᴏᴛ ʀᴇᴘᴏ  ➥ /repo)"
]

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/f6b2e18ecae7ffb6a9c88.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"
STATS_IMG_URL = "https://telegra.ph/file/7adee139f0639c400e1b8.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/9e14789c344a3c983aca5.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/9e14789c344a3c983aca5.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/9e14789c344a3c983aca5.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
