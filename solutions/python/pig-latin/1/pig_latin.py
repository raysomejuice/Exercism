def translate(text: str) -> str:
    """Translate a test from English to Pig Latin.
    
    :param text: str - The original English word.
    :return: str - The word in Pig Latin.
    """
    phrase = text.split()
    result = []

    for word in phrase:
        if word[0] in 'aeiou' or word[:2] in ('xr', 'yt'):
            result.append(word + 'ay')
            continue

        for char in word[1:]:
            if char in 'aeiouy':
                index = word.find(char)
                break
    
        if word.find('qu') != -1:
            index = word.find('qu') + 2

        result.append(word[index:] + word[:index] + 'ay')
    
    return ' '.join(result)
