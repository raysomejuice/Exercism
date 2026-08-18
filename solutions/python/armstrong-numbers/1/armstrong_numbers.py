
        
def is_armstrong_number(number: int) -> bool:
    """Determine if entered number is an armstrong number
    :param int: number - the number entered
    :return: bool - TRUE if an armstrong number
    """    
    changed_to_string = str(number)
    return number == sum([int(digit) ** len(changed_to_string) for digit in changed_to_string])