def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """Identify anagrams to a target word from a list of candidates

    :param word: str - The target word to find anagrams
    :param candidates: list[str] - words that are possible anagrams
    :return: list[str] - Anagrams found
    """
    list_of_anagrams = []
    low_word = word.lower()

    for item in candidates:
        low_item = item.lower()
        if low_item != low_word and sorted(low_item) == sorted(low_word):
            list_of_anagrams.append(item)

    return list_of_anagrams
