BAND_COLORS = ['black', 'brown', 'red', 'orange', 'yellow',
               'green', 'blue', 'violet', 'grey', 'white']


def color_code(color: str) -> int:
    """Determine the numerical value for any color on a resistor.
    
    :param color: str - the color of a stripe on a resistor
    :return: int - the value associated with given color.
    """
    return BAND_COLORS.index(color)


def value(colors: list[str]) -> int:
    """Determine the value of the first two colors of a resistor.
    
    :param colors: list[str] - the color inputs of a resistor (various number)
    :return: int - the value of the first two colors"""
    first, second, *_ = colors
    return int(str(BAND_COLORS.index(first)) + str(BAND_COLORS.index(second)))


def label(colors: list[str]) -> str:
    """Determine the resistance value to put on the label of a resistor
    
    :param colors: list[str] - the color stripes on a resistor
    :return: str - the resistance value for the label
    """
    first, second, power, *_ = colors
    resistance = value([first, second]) * (10 ** color_code(power))

    if not resistance:
        return '0 ohms'
        
    if resistance % (10 ** 9) == 0:
        num = resistance // (10 ** 9)
        metric = 'giga'
    elif resistance % (10 ** 6) == 0:
        num = resistance // (10 ** 6)
        metric = 'mega'
    elif resistance % (10 ** 3) == 0:
        num = resistance // (10 ** 3)
        metric = 'kilo'
    else:
        num = resistance
        metric = ''

    return '{} {}ohms'.format(num, metric)
