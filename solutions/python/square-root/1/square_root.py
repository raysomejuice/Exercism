def square_root(number: int) -> float:
    counter = 1
    while counter ** 2 <= number:
        approx = counter
        counter += 1

    while approx ** 2 != number:
        approx = (approx + (number / approx)) / 2

    return approx
