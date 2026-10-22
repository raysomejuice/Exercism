def egg_count(display_value: int) -> int:
    power_of_two = 1
    while power_of_two * 2 < display_value:
        power_of_two *= 2
    eggs = 0
    while display_value > 0:
        if display_value >= power_of_two:
            eggs += 1
        display_value %= power_of_two
        power_of_two //= 2

    return eggs
