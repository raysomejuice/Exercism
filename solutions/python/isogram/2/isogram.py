def is_isogram(string: str) -> bool:
    """Determine if the input string is an isogram.
    An isogram is a word or phrase that uses each letter in it only once.
    
    :param string - the input string to identify as an isogram or not.
    :return: - TRUE if an isogram or FALSE if not
    """
    cleaned_string = [x for x in string.lower() if x.isalpha()]
    return len(cleaned_string) == len(set(cleaned_string))
