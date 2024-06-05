from KRISHMUSIC.core.bot import JARVIS
from KRISHMUSIC.core.dir import dirr
from KRISHMUSIC.core.git import git
from KRISHMUSIC.core.userbot import Userbot
from ANNIEMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = JARVIS()
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
