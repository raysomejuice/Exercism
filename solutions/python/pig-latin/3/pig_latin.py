def piggify(word: str) -> str:
    """The rules for converting a single word to Pig Latin.
    :param word: str - A single word.
    :return: str - The word in Pig Latin.
    """
    if word[:1] in 'aeiou' or word[:2] in ('xr', 'yt'):
        return word + 'ay'

    word_iterator = iter(word[1:])
    char = next(word_iterator)
    
    while char not in 'aeiouy':
        char = next(word_iterator)

    index = word.find(char)
    
#    index = min(word.find(char) for char in word[1:] if char in 'aeiouy')
    
    if word.find('qu') != -1:
        if word.find('qu') < index:
            index = word.find('qu') + 2
        
    return word[index:] + word[:index] + 'ay'


def translate(text: str) -> str:
    """Translate a text from English to Pig Latin.
    
    :param text: str - The original English text.
    :return: str - The text in Pig Latin.
    """
    phrase = text.split()
    result = [piggify(word) for word in phrase]
    return ' '.join(result)
