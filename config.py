import os


class Config(object):
    API_HASH = os.environ.get("9ff4a51876a555bdb530cd6a58baae87")
    BOT_TOKEN = os.environ.get("5979051635:AAFXtaM-unQFsD8rHCXj8FMF9cDsDSPNzyQ")
    TELEGRAM_API = os.environ("1954515")
    OWNER = os.environ.get("800555393")
    OWNER_USERNAME = os.environ.get("ajithvnr")
    PASSWORD = os.environ.get("0000asdf")
    DATABASE_URL = os.environ.get("mongodb+srv://botvnr:BqyoAN11n7ilmhN9@cluster0.7ve9yva.mongodb.net/")
    LOGCHANNEL = os.environ.get("-1001616814441")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
