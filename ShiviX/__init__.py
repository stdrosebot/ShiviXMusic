from ShiviX.core.bot import ShiviXBot
from ShiviX.core.dir import dirr
from ShiviX.core.git import git
from ShiviX.core.userbot import Userbot
from ShiviX.misc import dbb, heroku, sudo
from aiohttp import ClientSession

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = ShiviXBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()
