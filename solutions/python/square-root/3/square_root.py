def square_root(number: int) -> float:
#    counter = 0
#    while counter * counter < number:
#        counter += 1
#        approx = counter
        
    approx = 1
    accepted_error = 0.000000000000001
    
    while abs(approx * approx - number) > accepted_error:
        approx = (approx + (number / approx)) / 2

    return approx
