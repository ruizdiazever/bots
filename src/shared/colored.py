def colored(text: str, color: str) -> str:
    """
    Return string in color with ANSI code
    """

    if color == "red":
        text = f"\033[91m{text}\033[00m"
    elif color == "yellow":
        text = f"\033[93m{text}\033[00m"
    elif color == "green":
        text = f"\033[92m{text}\033[00m"
    elif color == "cyan":
        text = f"\033[96m{text}\033[00m"
    elif color == "gray":
        text = f"\033[90m{text}\033[00m"
    else:
        pass
    return text
