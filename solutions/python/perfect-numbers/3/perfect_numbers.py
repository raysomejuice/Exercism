import math


def classify(number: int) -> str:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if not isinstance(number, int) or number < 1:
        raise ValueError('Classification is only possible for positive integers.')
        
    stop = math.floor(math.sqrt(number))  # Used to optimize loop. Don't know how expensive this is.
    factors = set()
    
    if number > 1:
        factors.add(1)
    
    for value in range(2, stop + 1):  # Don't know if a while loop would be better
        if number % value == 0:
            factors.update([value, number // value])
            
    total = sum(factors)
    
    if total == number:
        return 'perfect'
    if total > number:
        return 'abundant'
    return 'deficient'    
