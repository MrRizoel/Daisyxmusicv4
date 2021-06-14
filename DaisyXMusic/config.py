import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
<<<<<<< Updated upstream
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "DaisyXupdates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/dcfdf612e499eef0e0b1f.png")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "DaisyXhelper")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "DaisySupport_Official")
PROJECT_NAME = getenv("PROJECT_NAME", "DaisyXMusic v4")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/teamdaisyx/daisyxmusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
=======
BOT_NAME = getenv("BOT_NAME", "Mr.Shinchan")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Shinchan_Updates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/544da923c008df67f98f4.png")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "ShinchanHelper_Bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Shinchan_Helper")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Shinchan_Support")
PROJECT_NAME = getenv("PROJECT_NAME", "ShinchanMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
ARQ_API_KEY = getenv("ARQ_API_KEY")
>>>>>>> Stashed changes
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
