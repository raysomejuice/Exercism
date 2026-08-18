import string


def answer(question: str) -> int:
    """Convert a simple math word problem into an arithmatic statement
    then solve. The answer should resolve as an integer.

    :param question: str - The math question to solve.
    :return: int - the integer answer to the word problem.
    """
    operators = {'plus', 'minus', 'multiplied', 'divided'}
    num = {'-'}
    num.update(string.digits)
    
    stripped = (
        question
            .replace('What is', '')
            .replace('?', '')
            .replace('by ', '')
            .lstrip(' ')
            .split(' ')
    )

    if stripped == ['']:
        raise ValueError("syntax error")

    if not all((set(i) <= num or i in operators) for i in stripped):
        raise ValueError("unknown operation")
    
    if not(set(stripped[0]) <= num and set(stripped[-1]) <= num):
        raise ValueError("syntax error")

    if len(stripped) == 1 and set(stripped[0]) <= num:
        return int(stripped[0])

    for i in range(len(stripped) - 1):
        if set(stripped[i]) <= num and set(stripped[i + 1]) <= num:
            raise ValueError("syntax error")
        if stripped[i] in operators and not(set(stripped[i - 1]) <= num):
            raise ValueError("syntax error")
        if stripped[i] in operators and not(set(stripped[i + 1]) <= num):
            raise ValueError("syntax error")


    result = int(stripped[0])
    
    for i in range(len(stripped) - 1):
        if stripped[i] == 'plus':
            result +=  int(stripped[i + 1])
        if stripped[i] == 'minus':
            result -=  int(stripped[i + 1])
        if stripped[i] == 'multiplied':
            result *=  int(stripped[i + 1])
        if stripped[i] == 'divided':
            result //=  int(stripped[i + 1])

    return result