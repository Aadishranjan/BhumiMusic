# Copyright (c) 2026 Aadish Ranjan <Aadishranjan>
# Location: India
#
# All rights reserved.
#
# This code is the intellectual property of Aadish Ranjan.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: aadishranjan35@gmail.com


from ShrutiMusic.core.bot import Nand
from ShrutiMusic.core.dir import dirr
from ShrutiMusic.core.git import git
from ShrutiMusic.core.userbot import Userbot
from ShrutiMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Nand()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()


# ©️ Copyright Reserved - @Aadishranjan  Aadish Ranjan

# ===========================================
# ©️ 2026 Aadish Ranjan (@Aadishranjan)
# 🔗 GitHub : https://github.com/Aadishranjan/BhumiMusic
# 📢 Telegram Channel : https://t.me/YutaxBots
# ===========================================


# ❤️ Love From BhumiMusic 