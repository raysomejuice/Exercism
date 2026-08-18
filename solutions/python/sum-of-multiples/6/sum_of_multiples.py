def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    """Calculate the total energy points a player earned after
    completing a game level.

    :param limit: int - the game level and points limit.
    :param multiples: int - the base point value for various
    magical items gather during level.
    :return: int - points earned that level.
    """
    return sum({mult_num for base_num in multiples if base_num 
                for mult_num in range(base_num, limit, base_num)})
