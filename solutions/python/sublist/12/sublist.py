"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def is_match[T](smaller: list[T], larger: list[T]) -> bool:
    """Determine if smaller is inside larger.
    
    :param smaller: list[T] - the smaller list of any value
    :param larger: list[T] - the larger list of any value
    :return: bool
    """
    len_large = len(larger)
    len_small = len(smaller)
    return any(
        larger[item : item + len_small] == smaller 
        for item in range(len_large - len_small + 1)
    )


def sublist[T](list_one: list[T], list_two: list[T]) -> int:
    """Determine how two list compare to each other.
    
    Either:
    List A is EQUAL to List B,
    List A is SUBLIST to List B,
    List A is SUPERLIST to List B, or
    List A is UNEQUAL to List B.
    :param list_one: list[T] - the first list of any value
    :param list_two: list[T] - the second list of any value
    :return: Compare - the values EQUAL, SUBLIST, SUPERLIST, or UNEQUAL
    """
    if list_one == list_two:
        return EQUAL

    if is_match(list_two, list_one):
        return SUPERLIST

    if is_match(list_one, list_two):
        return SUBLIST

    return UNEQUAL