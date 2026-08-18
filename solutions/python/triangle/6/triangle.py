def triangle(sides: tuple[int, int, int]) -> bool:
    """Determine if the sides can actually form a triangle first.

    :param sides: tuple - The lengths of the three sides as positive ints
    :return: bool - TRUE if equilateral or FALSE if not equilateral
    """
    a, b, c = sorted(sides)
    return (a > 0) and (a + b >= c)

def equilateral(sides: tuple[int, int, int]) -> bool:
    """Then determine if the triangle is equilateral.

    :param sides: tuple - The lengths of the three sides as positive ints
    :return: bool - TRUE if equilateral or FALSE if not equilateral
    """
    a, b, c = sides
    return triangle(sides) and (a == b) and (b == c)
    


def isosceles(sides: tuple[int, int, int]) -> bool:
    """Then determine if the triangle is isosceles.

    :param sides: tuple - The lengths of the three sides as positive ints
    :return: bool - TRUE if isosceles or FALSE if not isosceles
    """
    a, b, c = sides
    return triangle(sides) and (a == b) ^ (b == c) ^ (c == a)


def scalene(sides: tuple[int, int, int]) -> bool:
    """Then determine if the triangle is scalene.

    :param sides: tuple - The lengths of the three sides as positive ints
    :return: bool - TRUE if scalene or FALSE if not scalene
    """
    a, b, c = sides
    return triangle(sides) and (a != b and b != c and c != a)
