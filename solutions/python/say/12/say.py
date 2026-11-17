"""Takes a whole number and returns word form."""

UNDER_TWENTY_NAMES = {
    1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight",
    9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
    13: "thirteen", 14: "fourteen", 15: "fifteen",
    16: "sixteen", 17: "seventeen", 18: "eighteen",
    19: "nineteen"
}

TENS_NAMES = {
    2: "twenty", 3: "thirty", 4: "forty", 
    5: "fifty", 6: "sixty", 7: "seventy", 
    8: "eighty", 9: "ninety"
}

PLACE_NAMES = {
   1: "thousand", 2: "million", 3: "billion"
}


def say(number: int) -> str:
    """Converts a whole number into English words.
    
        :param number: int - whole number between 0 and 999,999,999,999
        :return: str - the number in word form
    """
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    word_numbers = []
    number_split_by_thousands = []

    while number > 0:
        number_split_by_thousands.append(number % 1000)
        number = number // 1000

    for index, split in reversed(list(enumerate(number_split_by_thousands))):

        if not split:
            continue
        
        hundreds, tens = divmod(split, 100)
        tens_place, ones = divmod(tens, 10)
        
        if hundreds:
            word_numbers.extend([UNDER_TWENTY_NAMES[hundreds], "hundred"]) 
            
        if tens:
            tens_word = ""
            if tens in UNDER_TWENTY_NAMES:
                tens_word = UNDER_TWENTY_NAMES[tens]
            elif tens_place in TENS_NAMES:
                tens_word = TENS_NAMES[tens_place]
                if ones:
                    tens_word += "-" + UNDER_TWENTY_NAMES[ones]

            word_numbers.append(tens_word)
            
        if index in PLACE_NAMES:
            word_numbers.append(PLACE_NAMES[index])

    return " ".join(word_numbers).strip()
            
    