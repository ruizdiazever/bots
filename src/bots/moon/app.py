import time
from src.bots.moon.core import get_data_coinbase, operation_output
from src.shared.telegram import api_telegram
from src.settings import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, INTERVAL


def start_moon():
    counter = 0
    try:
        while True:
            data = get_data_coinbase()
            operation_output(data, counter=counter)
            counter += 1
            time.sleep(INTERVAL)
    except Exception as error:
        msg = f"{type(error).__name__}: {str(error)}"
        api_telegram(TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, msg)
