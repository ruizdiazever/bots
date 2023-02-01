from src.shared.colored import colored


def set_output(title: str, body: str, extradata: str):
    """ Return a dictionary with colored and plain text """
    title_color = colored(title, "yellow")
    return {
        "colored": f"{title_color}: {body}\nHTML: {extradata}\n",
        "plain": f"{title}: {body}\nHTML: {extradata}\n"
    }


USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0",
    "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"
]

