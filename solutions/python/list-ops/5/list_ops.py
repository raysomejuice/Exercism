def append(list1, list2):
    return list1 + list2

        
def concat(lists):
    flat = []
    for item in lists:
        flat += item
    return flat

        
def filter(function, list):
    return [item for item in list if function(item)]

        
def length(list):
    counter = 0
    for item in list:
        counter += 1
    return counter

        
def map(function, list):
    return [function(item) for item in list]

        
def foldl(function, list, initial):
    accumulator = initial
    for item in list: 
        accumulator = function(accumulator, item)
    return accumulator

        
def foldr(function, list, initial):
    return foldl(function, list[::-1], initial)

        
def reverse(list):
    return list[::-1]