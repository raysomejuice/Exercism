# wanted to try to solve w/o converting to number into string

def count_digits(number: int) -> int:
    """Count number of digits recursively
    :param number: int - the number to have its digits counted
    :return: int - number of digits counted
    """
    counter = 1
    
    while number // 10 != 0:
        counter += 1
        number = number // 10

    return counter



def is_armstrong_number(number: int) -> bool:
    """Determine if entered number is an armstrong number
    :param int: number - the number entered
    :return: bool - TRUE if an armstrong number
    """
    num_of_digits = count_digits(number)
    # (number // (10 ** digit)) % 10 separates digits in number into list. 
    # Exponent num_of_digits is applied to each digit in list.
    # Values in list are added together.
    return number == sum([(((number // (10 ** digit)) % 10) ** num_of_digits) for digit in range(num_of_digits)]) 
