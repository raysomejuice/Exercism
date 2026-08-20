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


def sublist(list_one: list[int], list_two: list[int]) -> int:
    """Determine how two list compare to each other. Either:
    List A is EQUAL to List B,
    List A is SUBLIST to List B,
    List A is SUPERLIST to List B, or
    List A is UNEQUAL to List B.
    :param list_one: list[int] - the first list of integers
    :param list_two: list[int] - the second list of integers
    :return: Compare - the values EQUAL, SUBLIST, SUPERLIST, or UNEQUAL
    """
    len_one = len(list_one)
    len_two = len(list_two)

    if len_one == 0 and len_two > 0:
        return SUBLIST

    if  len_one > 0 and len_two == 0:
        return SUPERLIST
    
    if list_one == list_two:
        return EQUAL

    if len_one > len_two:
        verified_count = 0
        for i in range(len_one):
            for j in range(len_two):
                if list_one[i + j] == list_two[j] and len_one - (j + 1) >= len_two:
                    verified_count += 1
                else:
                    verified_count = 0
                    break
            if verified_count == len_two:
                return SUPERLIST

    if len_one < len_two:
        verified_count = 0
        for i in range(len_two):
            for j in range(len_one):
                if list_two[i + j] == list_one[j] and len_two - (j + 1) >= len_one:
                    verified_count += 1
                else:
                    verified_count = 0
                    break
            if verified_count == len_one:
                return SUBLIST
            
    return UNEQUAL