from typing import TypeVar

T = TypeVar('T')


def flatten(iterable: list[None | T | list[None | T]]) -> list[T]:
    """Make a single flattened list from a nested list without and null values
    
    :param iterable: list - The nested list to flatten
    :return: list - The flattened list
    """
    flat_list = []
    for item in iterable:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        elif item is not None:
            flat_list.append(item)
    return flat_list
