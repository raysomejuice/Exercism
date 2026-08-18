import queue

BRACKET_PAIRS = {'[' : ']',
                 '{' : '}',
                 '(' : ')'
                }


def is_paired(input_string: str) -> bool:
    """Determines if grouping symbols are appropriately paired.
    :param input_string: str - The string containing grouping symbols.
    :return: bool - Return TRUE if grouping symbols are appropriately paired.
    """
    bracket = queue.LifoQueue()

    for char in input_string:
        if char in BRACKET_PAIRS:
            bracket.put(char)
            
        if char in BRACKET_PAIRS.values():
            try:
                item = bracket.get_nowait()
                if BRACKET_PAIRS[item] != char:
                    return False
            except queue.Empty:
                return False
            
    return bracket.empty()
