def equilateral(sides: tuple[float, float, float]) -> bool:
    """Determine if the sides can actually form a triangle first.
    Then determine if the triangle is equilateral.

    :param sides: tuple - The lengths of the three sides as positive floats
    :return: bool - TRUE if equilateral or FALSE if not equilateral
    """
    a: float = sides[0]
    b: float = sides[1]
    c: float = sides[2]
    return (0 not in sides) and (sum(sides) == abs(sum(sides))) and (a + b >= c) and (b + c >= a) and (c + a >= b) and (a == b) and (b == c)
    


def isosceles(sides: tuple[float, float, float]) -> bool:
    """Determine if the sides can actually form a triangle first.
    Then determine if the triangle is isosceles.

    :param sides: tuple - The lengths of the three sides as positive floats
    :return: bool - TRUE if isosceles or FALSE if not isosceles
    """
    a: float = sides[0]
    b: float = sides[1]
    c: float = sides[2]
    return (0 not in sides) and (sum(sides) == abs(sum(sides))) and (a + b >= c) and (b + c >= a) and (c + a >= b) and (a == b or b == c or c == a)


def scalene(sides: tuple[float, float, float]) -> bool:
    """Determine if the sides can actually form a triangle first.
    Then determine if the triangle is scalene.

    :param sides: tuple - The lengths of the three sides as positive floats
    :return: bool - TRUE if scalene or FALSE if not scalene
    """
    a: float = sides[0]
    b: float = sides[1]
    c: float = sides[2]
    return (0 not in sides) and (sum(sides) == abs(sum(sides))) and (a + b >= c) and (b + c >= a) and (c + a >= b) and (a != b and b != c and c != a)
