def response(hey_bob: str) -> str:
    hey_bob = hey_bob.strip()

    if not hey_bob:
        return "Fine. Be that way!"
        
    questions = hey_bob.endswith('?')
    yelling = hey_bob.isupper()
    
    if questions and yelling:
        return "Calm down, I know what I'm doing!"
    if questions:
        return "Sure."
    if yelling:
        return "Whoa, chill out!"
    return "Whatever."
    