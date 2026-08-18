# Labeled parsing of lists to head and tail for readability.
# It appears that ternary operators cannot be used as a result.


def append(list1, list2):
    if not list2:
        return list1
    head = list2[0]
    tail = list2[1:]
    return append(list1 + [head], tail)


def concat(lists):
    if not lists:
        return []
    head = lists[0]
    tail = lists[1:]
    return list(head + concat(tail))
    

def filter(function, list):
    if not list:
        return []
    head = list[0]
    tail = list[1:]
    return ([head] if function(head) else []) + filter(function, tail)


def length(list):
    if not list:
        return 0
    tail = list[1:]
    return 1 + length(tail)


def map(function, list):
    if not list:
        return []
    head = list[0]
    tail = list[1:]
    return [function(head)] + map(function, tail)


def foldl(function, list, initial):
    if not list:
        return initial
    head = list[0]
    tail = list[1:]
    return foldl(function, tail, function(initial, head))
    

def foldr(function, list, initial):
    if not list:
        return initial
    head = list[0]
    tail = list[1:]
    return function(foldr(function, tail, initial), head)


def reverse(list):
    if not list:
        return []
    head = list[0]
    tail = list[1:]
    return reverse(tail) + [head]
