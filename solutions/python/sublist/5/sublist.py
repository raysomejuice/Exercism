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

from typing import Any

SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def is_match(smaller: list[Any], larger: list[Any]) -> bool:
    """Determine if smaller is inside larger.
    :param smaller: list[Any] - the smaller list of any value
    :param larger: list[Any] - the larger list of any value
    :return: bool
    """
    indices = [i for i in range(len(larger)) if larger[i] == smaller[0]]
    for item in indices:
        if len(smaller) <= len(larger[item:]):
            if larger[item : item + len(smaller)] == smaller:
                return True
    return False


def sublist(list_one: list[Any], list_two: list[Any]) -> int:
    """Determine how two list compare to each other. Either:
    List A is EQUAL to List B,
    List A is SUBLIST to List B,
    List A is SUPERLIST to List B, or
    List A is UNEQUAL to List B.
    :param list_one: list[Any] - the first list of any value
    :param list_two: list[Any] - the second list of any value
    :return: Compare - the values EQUAL, SUBLIST, SUPERLIST, or UNEQUAL
    """

    if list_one == list_two:
        return EQUAL

    if not list_one:
        return SUBLIST

    if not list_two:
        return SUPERLIST

    if len(list_one) > len(list_two):
        if is_match(list_two, list_one):
            return SUPERLIST

    if len(list_one) < len(list_two):
        if is_match(list_one, list_two):
            return SUBLIST

    return UNEQUAL