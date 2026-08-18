def piggify(word: str) -> str:
    """The rules for converting a single word to Pig Latin.
    :param word: str - A single word.
    :return: str - The word in Pig Latin.
    """
    if word[:1] in 'aeiou' or word[:2] in ('xr', 'yt'):
        return word + 'ay'

    word_iterator = iter(word[1:])
    char = next(word_iterator)
    
    index = next(word.find(char) for char in word[1:] if char in 'aeiouy')

    if word[index -1:index + 1] == 'qu':
        index += 1
        
    return word[index:] + word[:index] + 'ay'


def translate(text: str) -> str:
    """Translate a text from English to Pig Latin.
    
    :param text: str - The original English text.
    :return: str - The text in Pig Latin.
    """
    return ' '.join(piggify(word) for word in text.split())
