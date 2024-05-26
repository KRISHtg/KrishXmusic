from AarohiX.core.bot import Dil
from AarohiX.core.dir import dirr
from AarohiX.core.git import git
from AarohiX.core.userbot import Userbot
from AarohiX.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Dil
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
APP = "tg_vc_bot"  # connect music api key "Dont change it"
