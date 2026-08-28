import string

def rows(letter: str) -> list[str]:
    """The diamond kata takes as its input a letter, and 
    outputs it in a diamond shape.
    
    Given a letter, it prints a diamond starting with 'A', 
    with the supplied letter at the widest point.
    param letter: str - the letter to build out to
    :return: list[str] - the list of string
    """
    letter_index = string.ascii_uppercase.index(letter)
    diamond_letters = (string.ascii_uppercase[:letter_index + 1]
                       + string.ascii_uppercase[:letter_index][::-1])
    dimensions = len(diamond_letters)
    diamond_rows = []

    for row, char in enumerate(diamond_letters):
        diff = abs(letter_index - row)
        if diff < letter_index:
            row_string = (char + (' ' * (dimensions - 2 * diff - 2))
                          + char).center(dimensions)
        else:
            row_string = char.center(dimensions)

        diamond_rows.append(row_string)

    return diamond_rows
