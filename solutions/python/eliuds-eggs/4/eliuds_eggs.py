def egg_count(display_value: int) -> int:
    '''Convert a base-10 number into a base-2 number. Then count 
    and display the number of 1's in base-2 number. The number of 
    1's reveal the number of eggs Eluid has.
    :param display_value: int - the base-10 number displayed
    :return: int - the number of 1's counted in base-2 number. 
    >>> egg_count(89)
    4
    >>> egg_count(16)
    1
    '''
    eggs = []
    while display_value > 0:
        eggs.append(display_value % 2)
        display_value //= 2
    return sum(eggs)
