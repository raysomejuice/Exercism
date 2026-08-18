def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    """Reformat the legacy data, which is a one-to-many match of score
    to list of letters, to one-to-one match of letter to score.

    :param legacy_data: dict[int, list[str]] - the original data
    :return: dict[str, int] - the reformatted data
    """
#    reformatted_data = {}
#    for score, letters in legacy_data.items():
#        for letter in letters:
#            reformatted_data[letter.lower()] = score

#    return reformatted_data
    return {letter.lower():score for score, letters in legacy_data.items()
            for letter in letters}
