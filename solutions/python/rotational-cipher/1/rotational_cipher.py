import string


def rotate(text: str, key: int) -> str:
    """An implementation of the rotational cipher.
    Rotate all the letters with the proper case of the original statement.
    Spaces and punctuation should remain unchanged.

    :param text: str - the original input statement
    :param key: int - the rotational shift

    :return: str - the ciphered output statement
    """
    string_list = list(text)
    upper = list(string.ascii_uppercase)
    lower = list(string.ascii_lowercase)
    ciphered = []

    for x in string_list:
        if x.islower():
            ciphered.append(lower[(lower.index(x) + key) % 26])
        elif x.isupper():
            ciphered.append(upper[(upper.index(x) + key) % 26])
        else:
            ciphered.append(x)

    return ''.join(ciphered)
