import string


def rotate(text: str, key: int) -> str:
    """An implementation of the rotational cipher.
    Rotate all the letters with the proper case of the original statement.
    Spaces and punctuation should remain unchanged.

    :param text: str - the original input statement
    :param key: int - the rotational shift

    :return: str - the ciphered output statement
    """
    all_caps = string.ascii_uppercase
    plain = all_caps + all_caps.lower()
    
    front = all_caps[key:] + all_caps[:key]
    cipher = front + front.lower()

    return text.translate(str.maketrans(plain, cipher))
