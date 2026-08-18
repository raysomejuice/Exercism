import math

def score(x: float, y: float) -> float:
    dart_dist = x * x + y * y
    inner_circle = 1
    middle_circle = 5
    outer_circle = 10

    if dart_dist <= inner_circle * inner_circle:
        return 10
    if dart_dist <= middle_circle * middle_circle:
        return 5
    if dart_dist <= outer_circle * outer_circle:
        return 1

    return 0
