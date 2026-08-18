def is_pangram(sentence: str) -> bool:
    """Determine if a sentence is a pangram.
    
    :param sentence: str - The original input sentence.
    :return: bool - TRUE if the sentence is a pangram.
    """
    only_alpha = set(x for x in sentence.lower() if x.isalpha())
    return len(only_alpha) == 26
    
