def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    """Calculate the total energy points a player earned after
    completing a game level.

    :param limit: int - the game level and points limit.
    :param multiples: int - the base point value for various
    magical items gather during level.
    :return: int - points earned that level.
    """
    return sum({val for base in multiples if base 
                for val in range(base, limit, base)})
