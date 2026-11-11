"""Takes a whole number and returns word form."""

ONES_NAMES = {
    "1": "one", "2": "two", "3": "three", "4": "four",
    "5": "five", "6": "six", "7": "seven", "8": "eight",
    "9": "nine"
}

TEENS_NAMES = {
    "10": "ten", "11": "eleven", "12": "twelve",
    "13": "thirteen", "14": "fourteen", "15": "fifteen",
    "16": "sixteen", "17": "seventeen", "18": "eighteen",
    "19": "nineteen"
}

TENS_NAMES = {
    "2": "twenty", "3": "thirty", "4": "forty", 
    "5": "fifty", "6": "sixty", "7": "seventy", 
    "8": "eighty", "9": "ninety"
}

PLACE_NAMES = {
    2: "hundred", 3: "thousand",  
    5: "hundred", 6: "million", 8: "hundred", 
    9: "billion", 11: "hundred"
}

TENS_PLACES =(1, 4, 7, 10)
HUNDREDS_PLACES = (2, 5, 8, 11)
THOUSANDS_PLACES = (3, 6, 9)

def say(number: int) -> str:
    """Converts a whole number into English words.
    
        :param number: int - whole number between 0 and 999,999,999,999
        :return: str - the number in word form
    """
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    word_numbers = []
    
    number = str(number)[::-1]
    num_length = len(number)
    for index in reversed(range(num_length)):
        if num_length == 1:
            if number[0] == "0":
                return "zero"
            return ONES_NAMES[number[0]]

        if index in TENS_PLACES:
            continue

        if index + 1 < num_length and index + 1 in TENS_PLACES:
            tens, ones = number[index: index + 2][::-1]
            if tens + ones == "00":
                continue
            if tens == "0":
                word_numbers.append(ONES_NAMES[ones])
            elif tens == "1":
                word_numbers.append(TEENS_NAMES[tens + ones])
            elif ones == "0":
                word_numbers.append(TENS_NAMES[tens])
            else:
                word_numbers.append(TENS_NAMES[tens] + "-" + ONES_NAMES[ones])

        elif number[index] in ONES_NAMES:
            word_numbers.append(ONES_NAMES[number[index]])
            
        if index in HUNDREDS_PLACES and number[index] != "0":
            word_numbers.append(PLACE_NAMES[index])

        if index in THOUSANDS_PLACES and number[index:index + 3] != "000":
            word_numbers.append(PLACE_NAMES[index])

    return " ".join(word_numbers).strip()
            
    