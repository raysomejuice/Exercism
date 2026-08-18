def leap_year(year: int) -> bool:
    """Determine whether or not a given year is a leap year

    :param year: int - What year in the Gregorian calendar is it?
    :return: bool - TRUE if a leap year or FALSE if not a leap year
    """
    return (year % 400 == 0) or ((year % 4 == 0 and year % 100 != 0))
