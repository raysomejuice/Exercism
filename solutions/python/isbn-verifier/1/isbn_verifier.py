def is_valid(isbn: str) -> bool:
    """Determine if the inputted ISBN-10 is valid.
    
    :param str: isbn -  the inputted ISBN-10 string
    return: bool - TRUE if valid, FALSE if not
    """
    length = 10
    
    isbn_cleaned = isbn.replace('-', '')
    
    if len(isbn_cleaned) != length:
        return False
        
    if not isbn_cleaned[:length - 1].isdigit():
        return False    
    
    if not isbn_cleaned[-1].isdigit():
        if not isbn_cleaned.endswith('X'):
            return False

    isbn_list = [int(i) if i != 'X' else 10 for i in isbn_cleaned]
    isbn_check = sum(j * (length - i) for i, j in enumerate(isbn_list))

    return isbn_check % 11 == 0
