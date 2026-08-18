def square_of_sum(number: int) -> int:
    # Used multiplication (*) instead of exponential (**) for performance
    return sum(i + 1 for i in range(number)) * sum(i + 1 for i in range(number))


def sum_of_squares(number: int) -> int:
    # Used multiplication (*) instead of exponential (**) for performance
    return sum((i + 1) * (i + 1) for i in range(number))


def difference_of_squares(number: int) -> int:
    return square_of_sum(number) - sum_of_squares(number)
