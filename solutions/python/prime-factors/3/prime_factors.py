"""Find the prime factors of any natural number."""


def factors(value: int) -> list[int]:
    """Input a natural number and outputs a list of prime factors.

    :param value: int - The natural number entered.
    :return: list[int] - The list of prime factors.
    """
    factor = 2
    primes = []
    while factor * factor <= value:
        while value % factor == 0:
            primes.append(factor)
            value //= factor
        
        factor += 1

    if value > 1:
        primes.append(value)
            
    return primes
