def is_isogram(string: str) -> bool:
    remove = str.maketrans('', '', ' -')
    cleaned_string = string.translate(remove).lower()
    return len(cleaned_string) == len(set(cleaned_string))
