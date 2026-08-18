import queue


def is_paired(input_string: str) -> bool:
    """Determines if grouping symbols are appropriately paired.
    :param input_string: str - The string containing grouping symbols.
    :return: bool - Return TRUE if grouping symbols are appropriately paired.
    """
    bracket = queue.LifoQueue()

    for char in input_string:
        if char == '[' or char == '{' or char == '(':
            bracket.put(char)
        if char == ']' or char == '}' or char == ')':
            try:
                item = bracket.get_nowait()
                if char == ']' and item != '[' or \
                   char == '}' and item != '{' or \
                   char == ')' and item != '(':
                    return False
            except queue.Empty:
                return False
            
    return bracket.empty()
