def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    """Calculate the total energy points a player earned after
    completing a game level.

    :param limit: int - the game level and points limit.
    :param multiples: int - the base point value for various
    magical items gather during level.
    :return: int - points earned that level.
    """
    points = set()
    for base in multiples:
        if base:
            n: int = 1
            while (base * n) < limit:
                points.add(base * n)
                n += 1

    return sum(points)
