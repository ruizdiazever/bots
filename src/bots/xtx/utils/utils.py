from src.shared.colored import colored


def set_output(title: str, body: str, extradata: str):
    """ Return a dictionary with colored and plain text """
    title_color = colored(title, "yellow")
    return {
        "colored": f"{title_color}: {body}\nHTML: {extradata}\n",
        "plain": f"{title}: {body}\nHTML: {extradata}\n"
    }

