import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", 21979881))
API_HASH = getenv("API_HASH", "ae5eac8daa75014fa597f5e1ca0d8655")
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "KRISH")
# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "8152673963:AAGmmeW-wAYaEZooTL1eHluLjC0xLZCdZaQ")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Krishopkyt:Krishopkyt@opkrish.jw1hi.mongodb.net/?retryWrites=true&w=majority&appName=Opkrish")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1001921995918))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6745609407))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Krishopmp/AnonXMusickrishbot",
)
REPO = getenv("REPO", "https://github.com/KRISHtg/AarohiX")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/DEV_UPDATE")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/FRIENDSOFHEAVEN")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes
KRISH = [
    "💣",
    "🚗",
    "🚕",
    "🚓",
    "🚑",
    "🧨"
    "💞", "𝚃𝙷𝙸𝚂 𝚂𝙾𝙽𝙶 𝙸𝚂 𝚃𝙾𝚃𝙰𝙻𝙻𝚈 𝙵𝙰𝙱𝚄𝙻𝙰𝚂𝚃𝙸𝙲...🔥🥰", "🔍", "🧪", "ʜᴏʟᴅ ᴏɴ ᴅᴀʀʟɪɴɢ 💗", "⚡️", "🔥", "ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...❤‍🔥", "🎩", "🌈", "⚡", "🐝", "🦋", 
    "ᴀᴄᴄʜɪ ᴘᴀsᴀɴᴅ ʜᴀɪ 🥰", "ʟᴏᴏᴋɪɴɢ ғᴏʀ ʏᴏᴜʀ sᴏɴɢ... ᴡᴀɪᴛ! 💗", "🪄", "ᴏᴋ ʙᴀʙʏ ᴡᴀɪᴛ😘 ғᴇᴡ sᴇᴄᴏɴᴅs", "ᴀʜʜ! ɢᴏᴏᴅ ᴄʜᴏɪᴄᴇ ʜᴏʟᴅ ᴏɴ...",  
    "ᴡᴏᴡ! ɪᴛ's ᴍʏ ғᴀᴠᴏʀɪᴛᴇ sᴏɴɢ...", "ɴɪᴄᴇ ᴄʜᴏɪᴄᴇ..! ᴡᴀɪᴛ 𝟸 sᴇᴄᴏɴᴅ", "🔎", "🍹", "🍻", "ɪ ʟᴏᴠᴇ ᴛʜᴀᴛ sᴏɴɢ..!😍", "💥", "💗", "✨"
]

# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQFE4E4AqTDIRJzgXnkW6P6cmaGoODblWcgclDHb3DX5HjtPaNDWP6iOlFXV9HGJjax-ScODQ7GMzOnEidBrJfmU9GfvPmwmEpKuBaONr1_V5lvtwGBQjPQAFB95d8jxG8YO9lx7lJHqml3I4AyDxZmCRz-KIuR52Cc3sd86leTtIWSHnX000HU9BTvxBldMKLOfrhAMR-IHB51EoPj8Oz-rH82gfx1k3KAVX5qX3QGPP2rf-3v-PVsi_QEsc77Lg0soZ39uj0JNTa28c8Uyh1yCXk0o-d3cTRkXmRDvvyiCy0F0vcXK5RwrZrqmr_i5cPCJG6g8Q61FC6tf1AppsNXhy0zz8AAAAAGvZ6kYAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://envs.sh/0-8.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://i.ibb.co/B2gGTG0/photo-2024-09-14-04-06-37-7414345353811460116.jpg"
)
PLAYLIST_IMG_URL = "https://envs.sh/0-7.jpg"
STATS_IMG_URL = "https://i.ibb.co/pjPB26t/photo-2024-09-14-04-15-26-7414347630144126980.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
TELEGRAM_VIDEO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


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
        
