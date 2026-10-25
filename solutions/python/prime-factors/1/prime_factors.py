"""Find the prime factors of any natural number."""

def factors(value: int) -> list[int]:
    """Input a natural number and outputs a list of prime factors.

    :param value: int - The natural number entered.
    :return: list[int] - The list of prime factors.
    """
    factor = 2
    factors = []
    while value > 1:
        if value % factor:
            factor += 1
        else:
            factors.append(factor)
            value //= factor
    return factors
