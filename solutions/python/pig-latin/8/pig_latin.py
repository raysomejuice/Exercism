def find_first_vowel_or_y_index_after_first_letter(word: str) -> int:
    """Return the index of the first vowel or y after the first letter
    of a word.
    :param word: str - A single word.
    :return: int - the index of the first vowel found.
    """
    return next(word.find(char) for char in word[1:] if char in 'aeiouy')


def piggify(word: str) -> str:
    """The rules for converting a single word to Pig Latin.
    :param word: str - A single word.
    :return: str - The word in Pig Latin.
    """
    if word[:1] in 'aeiou' or word[:2] in ('xr', 'yt'):
        return word + 'ay'

    index = find_first_vowel_or_y_index_after_first_letter(word)

    if word[index -1:index + 1] == 'qu':
        index += 1
        
    return word[index:] + word[:index] + 'ay'


def translate(text: str) -> str:
    """Translate a text from English to Pig Latin.
    
    :param text: str - The original English text.
    :return: str - The text in Pig Latin.
    """
    return ' '.join(piggify(word) for word in text.split())
