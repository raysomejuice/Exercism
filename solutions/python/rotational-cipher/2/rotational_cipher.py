import string


def rotate(text: str, key: int) -> str:
    """An implementation of the rotational cipher.
    Rotate all the letters with the proper case of the original statement.
    Spaces and punctuation should remain unchanged.

    :param text: str - the original input statement
    :param key: int - the rotational shift

    :return: str - the ciphered output statement
    """
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    
    plain = upper + lower
    cipher = upper[key:] + upper[:key] + lower[key:] + lower[:key]

    return text.translate(str.maketrans(plain, cipher))
