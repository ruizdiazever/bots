import logging
import requests, random, time
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import pytz
from src.core.xtx.core import USER_AGENTS
from src.settings import TELEGRAM_CHAT_ID, TELEGRAM_TOKEN, TIMEZONE, XTX_CONFIG
from src.core.xtx.core import set_output
from src.shared.telegram import api_telegram


# LOGGING
logging.basicConfig(filename='src/logs/xtx.log', level=logging.INFO, format="")


# CONSTANTS
SEPARATOR = "-" * 80
TIMEZONE_OBJ = pytz.timezone(TIMEZONE)
LINKS = XTX_CONFIG["url"]
ACTIVE = XTX_CONFIG["active"]
INTERVAL_MIN = XTX_CONFIG["interval"]["min"]
INTERVAL_MAX = XTX_CONFIG["interval"]["max"]
RANDOM_DELAY = random.randint(INTERVAL_MIN, INTERVAL_MAX)


# MAIN
def start_xtx():
    if bool(int(ACTIVE)):
        while True:
            now = datetime.now(tz=TIMEZONE_OBJ)
            now_formatted = now.strftime('%d/%m/%Y %H:%M')
            print(f"{now_formatted:^80}")
            print(SEPARATOR)
            logging.info(now_formatted)
            logging.info(SEPARATOR)
            for link in LINKS:
                random_user_agent = random.choice(USER_AGENTS)
                headers = {'User-Agent': random_user_agent}
                if link["active"]:
                    try:
                        response = requests.get(link["url"], timeout=5, headers=headers)
                        soup = BeautifulSoup(response.text, "html.parser")

                        if link["type"] == "id":
                            availability = soup.find(id=link["typeKey"])
                        else:
                            availability = soup.find(class_=link["typeKey"])

                        list_result = []
                        if availability != None:
                            for text in availability.stripped_strings:
                                list_result.append(text)
                            if link["noStockString"] in list_result:
                                title = link["name"]
                                body = "RX 7900 XTX is out of stock"
                                extradata = list_result
                                result = set_output(title, body, extradata)
                            else:
                                title = link["name"]
                                body = "RX 7900 XTX is in stock"
                                extradata = list_result
                                result = set_output(title, body, extradata)
                                url = api_telegram(TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, result["plain"])
                                requests.get(url, timeout=10)
                        else:
                            result = set_output(link["name"], "Request failed", "None")
                        print(result["colored"])
                        logging.info(f"{result['plain']}")
                    except Exception as error:
                        result = set_output(link["name"], type(error).__name__, "None")
                        print(result["colored"])
                        logging.info(result["plain"])
            delay = RANDOM_DELAY * 60
            next_check = (now + timedelta(seconds=delay)).strftime('%d/%m/%Y %H:%M')
            msg_check = f"Next check at {next_check}"
            print(f"{msg_check:^80}")
            print(SEPARATOR)
            print(("\n" * 3))
            time.sleep(delay)
    else:
        print("Ant disable, you can active in config/xtx.yml")
