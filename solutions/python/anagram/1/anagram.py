def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """Identify anagrams to a target word from a list of candidates

    :param word: str - The target word to find anagrams
    :param candidates: list[str] - words that are possible anagrams
    :return: list[str] - Anagrams found
    """
    list_of_anagrams = []

    for item in candidates:
        item_val = sum(ord(c) for c in item.lower()) 
        word_val = sum(ord(c) for c in word.lower())
        if item.lower() == word.lower():
            continue
        if item_val != word_val:
            continue
        if len(item) == len(word) and set(item.lower()) == set(word.lower()):
            list_of_anagrams.append(item)

    return list_of_anagrams
