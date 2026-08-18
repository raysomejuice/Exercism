BAND_COLORS = {'black' : 0, 
               'brown' : 1, 
               'red' : 2, 
               'orange' : 3, 
               'yellow' : 4,
               'green' : 5, 
               'blue' : 6, 
               'violet' : 7, 
               'grey' : 8, 
               'white' : 9
              }

SI = {1000000000 : 'giga', 
      1000000 : 'mega', 
      1000 : 'kilo', 
      1 : ''
     }


def _value(colors: list[str]) -> int:
    """Determine the value of the first two colors of a resistor.
    
    :param colors: list[str] - the color inputs of a resistor (various number)
    :return: int - the value of the first two colors
    """
    bars = len(colors) - 1
    return sum(BAND_COLORS[j] * 10 ** (bars - i) for i, j in enumerate(colors))


def label(colors: list[str]) -> str:
    """Determine the resistance value to put on the label of a resistor
    
    :param colors: list[str] - the color stripes on a resistor
    :return: str - the resistance value for the label
    """
    first, second, power, *_ = colors
    resistance = _value([first, second]) * (10 ** BAND_COLORS[power])
    
    if resistance == 0:
        return '0 ohms'

    for factor, prefix in SI.items():
        if resistance % factor == 0:
            num = resistance // factor
            break

    return f'{num} {prefix}ohms'
