import math

def score(x: float, y: float) -> int:
    """Determine the score in a game of darts.

    :param x: float - the x-coordinate of where the dart lands on the target
    :param y: float - the y-coordinate of where the dart lands on the target

    :return: int - the score for hitting the target 
    """
    dart_dist_squared = x * x + y * y
    inner_circle = 1
    middle_circle = 5
    outer_circle = 10

    if dart_dist_squared <= inner_circle * inner_circle:
        return 10
    if dart_dist_squared <= middle_circle * middle_circle:
        return 5
    if dart_dist_squared <= outer_circle * outer_circle:
        return 1

    return 0
