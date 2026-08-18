BAND_COLORS = {'black' : 0, 'brown' : 1, 'red' : 2, 'orange' : 3, 'yellow' : 4,
               'green' : 5, 'blue' : 6, 'violet' : 7, 'grey' : 8, 'white' : 9}


def color_code(color: str) -> int:
    """Determine the numerical value for any color on a resistor.
    
    :param color: str - the color of a stripe on a resistor
    :return: int - the value associated with given color.
    """
    return BAND_COLORS[color]


def colors() -> list[str]:
    """List of all the colors used to determine resistor value
    
    :param: none
    :return: list[str] - all the colors used to determine resistor value
    """
    return list(BAND_COLORS.keys())
