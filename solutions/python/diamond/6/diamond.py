"""The diamond kata takes as its input a letter, and 
outputs it in a diamond shape."""

import string

def rows(letter: str) -> list[str]:
    """Given a letter, it prints a diamond starting with 'A', 
    with the supplied letter at the widest point.
    
    param letter: str - the letter to build out to
    :return: list[str] - the list of string
    """
    letter_index = string.ascii_uppercase.index(letter)
    diamond_letters = string.ascii_uppercase[:letter_index + 1]
    dimensions = 2 * letter_index + 1
    diamond_rows = []

    for row, char in enumerate(diamond_letters):
        row_string = list(" " * dimensions)
        diff = letter_index - row
        row_string[diff] = char
        row_string[dimensions - 1 - diff] = char
        diamond_rows.append("".join(row_string))

    diamond_rows.extend(diamond_rows[-2::-1])

    return diamond_rows
