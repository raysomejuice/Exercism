# wanted to try to solve w/o converting to number into string

def is_armstrong_number(number: int) -> bool:
    """Determine if entered number is an armstrong number
    :param int: number - the number entered
    :return: bool - TRUE if an armstrong number
    """
    num_of_digits = 1
    find_digits_num = number

    while find_digits_num // 10 != 0:
        num_of_digits += 1
        find_digits_num = find_digits_num // 10

    # (number // (10 ** digit)) % 10 separates digits in number into list. 
    # Exponent num_of_digits is applied to each digit in list.
    # Values in list are added together.
    return number == sum([(((number // (10 ** digit)) % 10) ** num_of_digits) for digit in range(num_of_digits)]) 
