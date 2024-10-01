import re
import os
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", 21979881))
API_HASH = getenv("API_HASH", "ae5eac8daa75014fa597f5e1ca0d8655")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7531498433:AAGl0UZRapY8dnCQr4wGQtLg3B-XITzqqkY")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Krishopkyt:Krishopkyt@opkrish.jw1hi.mongodb.net/?retryWrites=true&w=majority&appName=Opkrish")
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "krish")
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 900))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1001921995918"))

# Get this value from @BRANDRD_ROBOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6745609407"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/KRISHtg/AnonXMusic2",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/KRISHBOTS")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+Kus9t8btLPRhYzll")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Auto Gcast/Broadcast Handler (True = broadcast on , False = broadcast off During Hosting, Dont Do anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "bcfe26b0ebc3428882a0b5fb3e872473")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "907c6a054c214005aeae1fd752273cc4")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "2000"))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @BRANDEDSTRINGSESSION_BOT on Telegram
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
    "START_IMG_URL", "https://files.catbox.moe/g1oph9.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/e2dbc2.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/5gvrca.jpg"
STATS_IMG_URL = "https://files.catbox.moe/qt7y1v.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/ol4kru.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/bzojlb.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/rdevf1.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/rdevf1.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/b3gaf7.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/ka97p1.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/8hvkyx.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/orvrya.jpg"


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
