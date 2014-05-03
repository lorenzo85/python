# Compress function [1, 1, 0, 0, 0, 1] ==> Compress ==> [[2, 1], [3, 0], [1, 1]]
def pack(value, occurrences) :
    return [[value, occurrences]]

def process(aList, index, value, occurrences) :
    if(index >= len(aList)) :
        return pack(value, occurrences)
    elif(aList[index] != value) :
        return pack(value, occurrences) + process(aList, index + 1, aList[index], 1)
    else :
        return process(aList, index + 1, aList[index], occurrences + 1)

def compress(aList) :
    if(not aList) : return []
    return process(aList, 1, aList[0], 1)


# Test Run
aList = [1,1,0,1,1,1,1,1,0,0,0,0,0,0,1,0,0]
print(compress(aList))