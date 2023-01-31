""" Main module of bot """
import logging
from datetime import datetime, timedelta
import requests
from coinbase.wallet.client import Client
from src.shared.telegram import api_telegram
from src.settings import TELEGRAM_CHAT_ID, TELEGRAM_TOKEN, COINBASE_API_KEY, COINBASE_API_SECRET
from src.settings import CONFIG
from src.shared.colored import colored


# LOGGING
logging.basicConfig(filename='src/logs/moon.log', level=logging.INFO, format="")


def get_data_coinbase() -> dict:
    """
    Return a dict with currency data
        * price: float
        * name: string
        * max: float
        * min: float
    """

    currencies = CONFIG["moon"]["currencies"]
    output = []

    client = Client(COINBASE_API_KEY, COINBASE_API_SECRET, api_version="YYYY-MM-DD")
    for currency in currencies:
        price = client.get_buy_price(currency_pair = currency["key"])
        price = float(price["amount"])
        data = {
            "price": price,
            "name": currency["name"],
            "max": currency["max"],
            "min": currency["min"]
            }
        output.append(data)
    return output


def operation_output(data: list, counter=0, test=True):
    """
    Send a message alert with Telegram or WhatsApp

        * To WhatsApp a graphical environment is required
        * To Telegram is necessary your bot, see more in
            * https://core.telegram.org/bots
    """
    COL_1, COL_2 = "COIN", "PRICE"
    COL_3, COL_4 = "MIN", "MAX"
    SEPARATOR = f"{'-'*80:^80}"
    interval = CONFIG["moon"]['telegram']['interval']

    counter += 1
    now = f"CURRENT {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    after = f"""AFTER   {(datetime.now() +
            timedelta(seconds=interval)).strftime('%Y-%m-%d %H:%M:%S')}"""

    counter_str = f"# {counter}"
    count = colored(f"{counter_str:^80}", "yellow")
    date = colored(f"{now:^80}", "gray")
    after = colored(f"{after:^80}", "gray")
    title = colored(f"{COL_1:<20}{COL_2:>20}{COL_3:>20}{COL_4:>20}", "green")
    print(f"\n\n{count}\n{date}\n{after}\n{title}")
    print(SEPARATOR)

    # LOGGING
    if test:
        logging.info("%s", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        logging.info("%s", f"{COL_1:<20}{COL_2:>20}{COL_3:>20}{COL_4:>20}")
        logging.info(SEPARATOR)

    for currency in data:
        info_1 = f"{currency['name']:<20}{currency['price']:>20}"
        info_2 = f"{currency['min']:>20}{currency['max']:>20}"
        print(info_1 + info_2)

        if test:
            logging.info(info_1 + info_2)

        if currency['price'] >= currency["max"] or currency['price'] <= currency["min"]:
            msg = f"The price of {currency['name']} is €{currency['price']}"
            if CONFIG["moon"]['telegram']['state']:
                url = api_telegram(TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, msg)
                requests.get(url, timeout=10)
    logging.info("\n")
