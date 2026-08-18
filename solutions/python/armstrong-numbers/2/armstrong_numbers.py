# wanted to try to solve w/o converting to number into string

def count_digits(number: int) -> int:
    """Count number of digits recursively
    :param number: int - the number to have its digits counted
    :return: int - number of digits counted
    """
    return 1 if number // 10 == 0 else 1 + count_digits(number // 10)


def is_armstrong_number(number: int) -> bool:
    """Determine if entered number is an armstrong number
    :param int: number - the number entered
    :return: bool - TRUE if an armstrong number
    """
    num_of_digits = count_digits(number)
    
    list_of_digits = [((number // (10 ** digit)) % 10) for digit in range(num_of_digits)] # separates digits in number in list
    return number == sum([digit ** num_of_digits for digit in list_of_digits])
        
