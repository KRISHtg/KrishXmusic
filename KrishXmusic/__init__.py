from KrishXmusic.core.bot import Hotty
from KrishXmusic.core.dir import dirr
from KrishXmusic.core.git import git
from KrishXmusic.core.userbot import Userbot
from KrishXmusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Hotty()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "BRANDED_KUDI_BOT"  # connect music api key "Dont change it"
