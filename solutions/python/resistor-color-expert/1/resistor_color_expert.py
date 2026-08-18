BAND_COLORS = {'black' : 0, 'brown' : 1, 'red' : 2, 'orange' : 3, 'yellow' : 4,
               'green' : 5, 'blue' : 6, 'violet' : 7, 'grey' : 8, 'white' : 9}

TOLERANCE_COLORS = {'grey' : 0.05, 'violet' : 0.1, 'blue' : 0.25, 'green' : 0.5,
                    'brown' : 1, 'red' : 2, 'gold' : 5, 'silver' : 10}


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
    return int(''.join(str(color_code(i)) for i in colors))


def resistor_label(colors: list[str]) -> str:
    """Determine the resistance value to put on the label of a resistor
    
    :param colors: list[str] - the color stripes on a resistor
    :return: str - the resistance value for the label
    """
    if len(colors) == 1:
        return '{} ohms'.format(value(colors))

    if len(colors) == 4:
        first, second, power, tolerance = colors
        resistance = value([first, second]) * (10 ** color_code(power))

    if len(colors) == 5:
        first, second, third, power, tolerance = colors
        resistance = value([first, second, third]) * (10 ** color_code(power))

    si = {1000000000 : 'giga', 1000000 : 'mega', 1000 : 'kilo', 1 : ''}

    for factor, prefix in si.items():
        if resistance >= factor:
            num = resistance / factor
            if resistance % factor == 0:
                num = int(num)
            metric = prefix
            break

    return '{} {}ohms ±{}%'.format(num, metric, TOLERANCE_COLORS[tolerance])
