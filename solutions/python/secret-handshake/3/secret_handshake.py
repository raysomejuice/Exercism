from itertools import compress


ACTIONS = ['jump', 'close your eyes', 'double blink', 'wink']


def commands(binary_str: str) -> list[str]:
    """Take the binary string of number from 1 to 31 and 
    convert it to a sequence of actions in a secret handshake.
    
    :param binary_str: str - the binary equivalent of a number from 1 to 31
    :return: list[str] -  the sequence of actions of in the secret handshake.
    """
    binary_list = list(map(int, binary_str))
    secret_handshake = list(compress(ACTIONS, binary_list[1:]))
    return secret_handshake if binary_list[0] else secret_handshake[::-1]

