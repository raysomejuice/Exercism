def line_up(name: str, number: int) -> int:
    """Create a ticket with the name and ordinal number of the customer.
    
    :param name: str - the name of the customer
    :param number: int - the queue number of the customer
    :return: str
    """
    suffix = "th"
    output = "{0}, you are the {1} customer we serve today. Thank you!"

    if number % 10 == 1 and number % 100 != 11:
        suffix = "st"

    if number % 10 == 2 and number % 100 != 12:
        suffix = "nd"

    if number % 10 == 3 and number % 100 != 13:
        suffix = "rd"

    return output.format(name, str(number) + suffix)
    