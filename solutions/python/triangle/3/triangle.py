def triangle(sides: tuple[int, int, int]) -> bool:
    a, b, c = sides
    return (0 not in sides) and (sum(sides) == abs(sum(sides))) and (a + b >= c) and (b + c >= a) and (c + a >= b)

def equilateral(sides: tuple[int, int, int]) -> bool:
    """Determine if the sides can actually form a triangle first.
    Then determine if the triangle is equilateral.

    :param sides: tuple - The lengths of the three sides as positive ints
    :return: bool - TRUE if equilateral or FALSE if not equilateral
    """
    a, b, c = sides
    return triangle(sides) and (a == b) and (b == c)
    


def isosceles(sides: tuple[int, int, int]) -> bool:
    """Determine if the sides can actually form a triangle first.
    Then determine if the triangle is isosceles.

    :param sides: tuple - The lengths of the three sides as positive ints
    :return: bool - TRUE if isosceles or FALSE if not isosceles
    """
    a, b, c = sides
    return triangle(sides) and (a == b or b == c or c == a)


def scalene(sides: tuple[int, int, int]) -> bool:
    """Determine if the sides can actually form a triangle first.
    Then determine if the triangle is scalene.

    :param sides: tuple - The lengths of the three sides as positive ints
    :return: bool - TRUE if scalene or FALSE if not scalene
    """
    a, b, c = sides
    return triangle(sides) and (a != b and b != c and c != a)
