def two_fer(name: str = None) -> str:
    """Determine what to day when giving away extra cookie.
    
    :param name: str - the name of the person receiving extra cookie.
    :return: str - the message to the one receiving extra cookie.
    """
    return f"One for {name if name else 'you'}, one for me."