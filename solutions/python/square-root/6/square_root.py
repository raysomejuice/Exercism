def square_root(number: int) -> int:
    approx = 1
    accepted_error = 0.000000000000001
    
    while abs(approx * approx - number) > accepted_error:
        approx = (approx + (number // approx)) // 2

    return approx
