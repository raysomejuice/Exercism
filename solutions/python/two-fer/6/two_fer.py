def two_fer(name: str = 'you') -> str:
    """Determine what to day when giving away extra cookie.
    
    :param name: str - the name of the person receiving extra cookie.
    :return: str - the message to the one receiving extra cookie.
    """
    return f"One for {name}, one for me."