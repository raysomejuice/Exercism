BAND_COLORS = ['black', 'brown', 'red', 'orange', 'yellow',
               'green', 'blue', 'violet', 'grey', 'white']


def value(colors: list[str]) -> int:
    """Determine the value of the first two colors of a resistor.
    
    :param colors: list[str] - the color inputs of a resistor (various number)
    :return: int - the value of the first two colors"""
    first, second, *_ = colors
    return int(str(BAND_COLORS.index(first)) + str(BAND_COLORS.index(second)))
