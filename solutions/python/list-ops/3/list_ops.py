def append(list1, list2):
    return list1 if not list2 else append(list1 + [list2[0]], list2[1:])


def concat(lists):
    return [] if not lists else list(lists[0] + concat(lists[1:]))
    

def filter(function, list):
    if not list:
        return []
    head = list[0]  # used head variable to meet PEP-8 reqs
    tail = list[1:]  # used tail variable to meet PEP-8 reqs
    return ([head] if function(head) else []) + filter(function, tail)


def length(list):
    return 0 if not list else 1 + length(list[1:])


def map(function, list):
    return [] if not list else [function(list[0])] + map(function, list[1:])


def foldl(function, list, initial):
    if not list:
        return initial 
    return foldl(function, list[1:], function(initial, list[0]))
    

def foldr(function, list, initial):
    if not list:
        return initial
    return function(foldr(function, list[1:], initial), list[0])


def reverse(list):
    return [] if not list else reverse(list[1:]) + [list[0]]
