"""Given a name and a number, your task is to produce a sentence using 
that name and that number as an ordinal numeral. Yaʻqūb expects to use 
numbers from 1 up to 999.
"""

def line_up(name: str, number: int) -> int:
    """Create a ticket with the name and ordinal number of the customer.
    
    :param name: str - the name of the customer
    :param number: int - the queue number of the customer
    :return: str
    """

    suffix = ("th" if 11 <= number % 100 <= 13 
              else {1 : "st", 2 : "nd", 3 : "rd"}.get(number % 10, "th"))
    return (f"{name}, you are the {number}" 
            + f"{suffix} customer we serve today. Thank you!")
    