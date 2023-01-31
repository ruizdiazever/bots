import os
from dotenv import load_dotenv
import yaml
from yaml.loader import SafeLoader


load_dotenv(".env")


with open('config.yml') as file:
    CONFIG = yaml.load(file, Loader=SafeLoader)


TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
COINBASE_API_SECRET = os.environ.get("COINBASE_API_SECRET")
COINBASE_API_KEY = os.environ.get("COINBASE_API_KEY")
INTERVAL = CONFIG["moon"]["telegram"]["interval"]
DB_DATABASE = os.environ.get("DB_DATABASE")
DB_HOST = os.environ.get("DB_HOST")
DB_SCHEMA = os.environ.get("DB_SCHEMA")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_PORT = os.environ.get("DB_PORT")
EMAIL = os.environ.get("EMAIL")
PHONE = os.environ.get("PHONE")
DEBUG=bool(int(os.environ.get("DEBUG")))
TIMEZONE=CONFIG("TIMEZONE")
