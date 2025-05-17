import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = getenv("API_ID", "28928028")
API_HASH = getenv("API_HASH", "b097202e877124392f4851d215fa8f3a")

EVAL = list(map(int, getenv("EVAL", "0000000 0000000").split()))
# ------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "7552858898:AAEeGSYwdpW3-7Y6epKymON3li7zLizRRSE")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "Fuyubot")
# --------------------------------------------------------

#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Lord_ichigo:Roshni@cluster0.ytuss.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = getenv("DB_NAME", "fuyu")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002323856532))
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", 7678359785))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

API_URL = getenv("API_URL", 'https://api.thequickearn.xyz') #youtube song url
API_KEY = getenv("API_KEY", "30DxNexGenBots3898d2") # youtube song api key, get it from https://t.me/RahulTC

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/DEV-ZTX/Fuyu",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Intro_Of_Mine")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+Q1nKBQjbTVI2ZDI1")
# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://telegra.ph/Privacy-Policy-for-AviaxMusic-08-14")


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = getenv("STRING_SESSION", None)
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
    "START_IMG_URL", "https://graph.org/file/299b085f6a9cdeab7689d-b3a6b28acb80c830b0.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/af0b3ce0dd5eb51a531ed-eacf5c5972ceab2b7b.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/299b085f6a9cdeab7689d-b3a6b28acb80c830b0.jpg"
STATS_IMG_URL = "https://graph.org/file/299b085f6a9cdeab7689d-b3a6b28acb80c830b0.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/299b085f6a9cdeab7689d-b3a6b28acb80c830b0.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/299b085f6a9cdeab7689d-b3a6b28acb80c830b0.jpg"
STREAM_IMG_URL = "https://graph.org/file/299b085f6a9cdeab7689d-b3a6b28acb80c830b0.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/299b085f6a9cdeab7689d-b3a6b28acb80c830b0.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/299b085f6a9cdeab7689d-b3a6b28acb80c830b0.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/299b085f6a9cdeab7689d-b3a6b28acb80c830b0.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/299b085f6a9cdeab7689d-b3a6b28acb80c830b0.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/299b085f6a9cdeab7689d-b3a6b28acb80c830b0.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
