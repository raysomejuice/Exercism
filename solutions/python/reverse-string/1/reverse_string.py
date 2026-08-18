def reverse(text: str) -> str:
    """Reverse the string.
    
    :param text: str - the input string
    :return: str - the input string in reverse
    """
    stop = len(text)
    return "".join(text[i] for i in range(-1, -(stop + 1), -1))
