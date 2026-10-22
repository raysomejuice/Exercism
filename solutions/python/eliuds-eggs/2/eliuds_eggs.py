def egg_count(display_value: int) -> int:
    eggs = []
    while display_value > 0:
        eggs.append(display_value % 2)
        display_value //= 2
    return sum(eggs)
