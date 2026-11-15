"""Takes a whole number and returns word form."""

UNDER_TWENTY_NAMES = {
    1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight",
    9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
    13: "thirteen", 14: "fourteen", 15: "fifteen",
    16: "sixteen", 17: "seventeen", 18: "eighteen",
    19: "nineteen"
}

# ONES_NAMES = {
#     1: "one", 2: "two", 3: "three", 4: "four",
#     5: "five", 6: "six", 7: "seven", 8: "eight",
#     9: "nine"
# }

# TEENS_NAMES = {
#     10: "ten", 11: "eleven", 12: "twelve",
#     13: "thirteen", 14: "fourteen", 15: "fifteen",
#     16: "sixteen", 17: "seventeen", 18: "eighteen",
#     19: "nineteen"
# }

TENS_NAMES = {
    2: "twenty", 3: "thirty", 4: "forty", 
    5: "fifty", 6: "sixty", 7: "seventy", 
    8: "eighty", 9: "ninety"
}

PLACE_NAMES = {
    0: "", 1: "thousand", 2: "million", 3: "billion"
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

    num_of_thousands = len(number_split_by_thousands)

    for index in reversed(range(num_of_thousands)):
        hundreds, tens = divmod(number_split_by_thousands[index], 100)
        tens_place, ones = divmod(tens, 10)
        if hundreds > 0:
            word_numbers.extend([UNDER_TWENTY_NAMES[hundreds], "hundred"]) 
        if tens in UNDER_TWENTY_NAMES:
            word_numbers.append(UNDER_TWENTY_NAMES[tens])
        elif tens_place in TENS_NAMES and ones in UNDER_TWENTY_NAMES:
            word_numbers.append(TENS_NAMES[tens_place] 
                                + "-" + UNDER_TWENTY_NAMES[ones])
        elif tens_place in TENS_NAMES:
            word_numbers.append(TENS_NAMES[tens_place])
        elif ones in UNDER_TWENTY_NAMES:
            word_numbers.append(UNDER_TWENTY_NAMES[ones])
        if number_split_by_thousands[index] > 0:
            word_numbers.append(PLACE_NAMES[index])



    
    # number = str(number)[::-1]
    # num_length = len(number)

    # if num_length == 1:
    #     if number[0] == "0":
    #         return "zero"
    #     return ONES_NAMES[number[0]]
        
    # for index in reversed(range(num_length)):
    #     if index % 3 == 1:
    #         continue

    #     if index + 1 < num_length and index % 3 == 0:
    #         tens, ones = number[index: index + 2][::-1]
    #         if tens + ones == "00":
    #             continue
    #         if tens == "0":
    #             word_numbers.append(ONES_NAMES[ones])
    #         elif tens == "1":
    #             word_numbers.append(TEENS_NAMES[tens + ones])
    #         elif ones == "0":
    #             word_numbers.append(TENS_NAMES[tens])
    #         else:
    #             word_numbers.append(TENS_NAMES[tens] + "-" + ONES_NAMES[ones])

    #     elif number[index] in ONES_NAMES:
    #         word_numbers.append(ONES_NAMES[number[index]])
            
    #     if index % 3 == 2 and number[index] != "0":
    #         word_numbers.append(PLACE_NAMES[index])

    #     if index >= 3 and index % 3 == 0 and number[index:index + 3] != "000":
    #         word_numbers.append(PLACE_NAMES[index])

    return " ".join(word_numbers).strip()
            
    