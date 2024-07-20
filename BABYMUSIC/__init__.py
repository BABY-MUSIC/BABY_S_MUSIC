from BABYMUSIC.core.bot import BABY
from BABYMUSIC.core.dir import dirr
from BABYMUSIC.core.git import git
from BABYMUSIC.core.userbot import Userbot
from BABYMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = BABY()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
