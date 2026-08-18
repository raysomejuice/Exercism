def is_valid(isbn: str) -> bool:
    """Determine if the inputted ISBN-10 is valid.
    
    :param str: isbn -  the inputted ISBN-10 string
    return: bool - TRUE if valid, FALSE if not
    """
    length = 10
    
    isbn_list = list(isbn.replace('-', ''))

    if len(isbn_list) != length:
        return False
        
    if isbn_list[-1] == 'X':
        isbn_list[-1] = '10'
        
    if not all(i.isdigit() for i in isbn_list):
        return False    

    isbn_check = sum(int(j) * (length - i) for i, j in enumerate(isbn_list))

    return isbn_check % 11 == 0
