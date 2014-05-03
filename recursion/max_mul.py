# Print out a list of pairs of numbers whose product is more than 25
MIN_PRODUCT = 25

def condition(element1, element2) :
    if(element1 * element2 > MIN_PRODUCT) : return [element1, element2]
    else: return None

def operation(aList, value) :
    return filter(lambda x : x != None, map(lambda x : condition(x, value), aList))

def problem(aList, bList, pos) :
    if(len(bList) == pos) : return []
    else : return list(operation(aList, bList[pos])) + problem(aList, bList, pos + 1)


# Test Run
aList = [1, 7, 67, 2, 24]
bList = [1, 8]
print(problem(aList, bList, 0))