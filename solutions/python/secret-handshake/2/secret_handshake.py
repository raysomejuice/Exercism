ACTIONS = ('jump', 'close your eyes', 'double blink', 'wink')


def commands(binary_str: str) -> list[str]:
    """Take the binary string of number from 1 to 31 and 
    convert it to a sequence of actions in a secret handshake.
    
    :param binary_str: str - the binary equivalent of a number from 1 to 31
    :return: list[str] -  the sequence of actions of in the secret handshake.
    """
    secret_handshake = []

    for digit in range(-1, -(len(binary_str)), -1):
        if binary_str[digit] == '1':
            secret_handshake.append(ACTIONS[digit])

    if binary_str[0] == '1':
        secret_handshake.reverse()

    return secret_handshake
