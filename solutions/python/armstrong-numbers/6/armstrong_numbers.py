# wanted to try to solve w/o converting to number into string

def is_armstrong_number(number: int) -> bool:
    """Determine if entered number is an armstrong number
    :param int: number - the number entered
    :return: bool - TRUE if an armstrong number
    """
    num_of_digits = 0
    find_digits_num = number

    while find_digits_num != 0:
        num_of_digits += 1
        find_digits_num = find_digits_num // 10

    digits_list = []

    # (number // (10 ** digit)) % 10 separates digits in number into list. 
    # Exponent num_of_digits is applied to each digit in list.
    
    for digit in range(num_of_digits):
        digits_list.append((((number // (10 ** digit)) % 10) ** num_of_digits))

    return number == sum(digits_list) 
