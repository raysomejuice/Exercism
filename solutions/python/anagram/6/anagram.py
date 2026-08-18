def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """Identify anagrams to a target word from a list of candidates

    :param word: str - The target word to find anagrams
    :param candidates: list[str] - words that are possible anagrams
    :return: list[str] - Anagrams found
    """
    list_of_anagrams = []
    lower_word = word.lower()
    sort_word = sorted(lower_word)

    for item in candidates:
        lower_item = item.lower()
        if lower_item != lower_word and sorted(lower_item) == sort_word:
            list_of_anagrams.append(item)

    return list_of_anagrams
