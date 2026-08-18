BAND_COLORS = {'black' : 0, 'brown' : 1, 'red' : 2, 'orange' : 3, 'yellow' : 4,
               'green' : 5, 'blue' : 6, 'violet' : 7, 'grey' : 8, 'white' : 9}


def value(colors: list[str]) -> int:
    """Determine the value of the first two colors of a resistor.
    
    :param colors: list[str] - the color inputs of a resistor (various number)
    :return: int - the value of the first two colors
    """
    first, second, *_ = colors
    return int(str(BAND_COLORS[first]) + str(BAND_COLORS[second]))
