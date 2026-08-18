def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    """Reformat data, one-to-many format to one-to-one format.
    The legacy data is formatted as a one-to-many match of score
    to list of letters. The data is to be reformatted to one-to-one 
    match of letter to score.

    :param legacy_data: dict[int, list[str]] - the original data
    :return: dict[str, int] - the reformatted data
    """
    return {letter.lower() : score for score, letters in legacy_data.items()
        for letter in letters}
