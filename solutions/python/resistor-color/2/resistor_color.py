BAND_COLORS = ['black', 'brown', 'red', 'orange', 'yellow',
               'green', 'blue', 'violet', 'grey', 'white']


def color_code(color: str) -> int:
    """Determine the numerical value for any color on a resistor.
    
    :param color: str - the color of a stripe on a resistor
    :return: int - the value associated with given color.
    """
    return BAND_COLORS.index(color)


def colors() -> list[str]:
    """List of all the colors used to determine resistor value
    
    :param: none
    :return: list[str] - all the colors used to determine resistor value
    """
    return BAND_COLORS
