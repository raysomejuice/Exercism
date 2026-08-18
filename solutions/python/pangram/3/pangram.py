import string


def is_pangram(sentence: str) -> bool:
    """Determine if a sentence is a pangram.
    
    :param sentence: str - The original input sentence.
    :return: bool - TRUE if the sentence is a pangram.
    """
    only_alpha = set(string.ascii_lowercase)
    return only_alpha <= set(sentence.lower())
    
