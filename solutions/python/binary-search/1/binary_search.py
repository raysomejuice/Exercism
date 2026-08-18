def find(search_list: list[int], value: int) -> int:
    """Use binary search to find the index of a value in a list.
    
    :param search_list: list[int] - list to search
    :param value: int - item being searched for
    :return: int - the index number of the value searched for
    """
    front = 0
    end = len(search_list) - 1

    while front <= end:
        middle = front + (end - front) // 2

        if search_list[middle] == value:
            return middle

        if search_list[middle] < value:
            front = middle + 1
        else:
            end = middle - 1

    raise ValueError("value not in array")
    