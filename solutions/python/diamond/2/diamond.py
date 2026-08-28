import string

def rows(letter):
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
            row_string = f"{char}".center(dimensions)

        diamond_rows.append(row_string)

    return diamond_rows
