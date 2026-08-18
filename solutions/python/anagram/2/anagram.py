def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """Identify anagrams to a target word from a list of candidates

    :param word: str - The target word to find anagrams
    :param candidates: list[str] - words that are possible anagrams
    :return: list[str] - Anagrams found
    """
    list_of_anagrams = []

    for item in candidates:
        if item.lower() == word.lower():
            continue
        if sorted(item.lower()) == sorted(word.lower()):
            list_of_anagrams.append(item)

    return list_of_anagrams
