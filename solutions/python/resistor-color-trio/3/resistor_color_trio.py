BAND_COLORS = {'black' : 0, 'brown' : 1, 'red' : 2, 'orange' : 3, 'yellow' : 4,
               'green' : 5, 'blue' : 6, 'violet' : 7, 'grey' : 8, 'white' : 9}


def color_code(color: str) -> int:
    """Determine the numerical value for any color on a resistor.
    
    :param color: str - the color of a stripe on a resistor
    :return: int - the value associated with given color.
    """
    return BAND_COLORS[color]


def value(colors: list[str]) -> int:
    """Determine the value of the first two colors of a resistor.
    
    :param colors: list[str] - the color inputs of a resistor (various number)
    :return: int - the value of the first two colors"""
    first, second, *_ = colors
    return int(str(BAND_COLORS[first]) + str(BAND_COLORS[second]))


def label(colors: list[str]) -> str:
    """Determine the resistance value to put on the label of a resistor
    
    :param colors: list[str] - the color stripes on a resistor
    :return: str - the resistance value for the label
    """
    first, second, power, *_ = colors
    resistance = value([first, second]) * (10 ** color_code(power))

    si = {1000000000 : 'giga', 1000000 : 'mega', 1000 : 'kilo', 1 : ''}

    if not resistance:
        return '0 ohms'

    for factor, prefix in si.items():
        if resistance % factor == 0:
            num = resistance // factor
            metric = prefix
            break

    return '{} {}ohms'.format(num, metric)
