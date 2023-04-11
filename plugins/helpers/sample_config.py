import os

class Config(object):
    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    # Get from my.telegram.org
    API_ID = int(os.environ.get("API_ID", ""))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "")
