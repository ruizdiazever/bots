def api_telegram(token: str, chat_id: str, message: str) -> str:
    """ Return url to request with API Telegram """
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    return url
