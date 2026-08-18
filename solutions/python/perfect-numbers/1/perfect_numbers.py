from math import sqrt, floor

def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1 or not isinstance(number, int):
        raise ValueError("Classification is only possible for positive integers.")
        
    stop = floor(sqrt(number))
    factors = set()
    
    if number > 1:
        factors.add(1)
    
    for value in range(2, stop + 1):
        if number % value == 0:
            factors.update([value, number // value])
            
    total = sum(factors)
    
    if total == number:
        return 'perfect'
    if total > number:
        return 'abundant'
    return 'deficient'    
