# fibonacci(x, y)
STOP = 4000000

def fibonacci(x, y, stop) :
    sum = x + y
    if sum >= stop : return []
    else : return [sum] + fibonacci(y, sum, stop)

def filterNotEven(aList) :
    return list(filter(lambda x : not x % 2, aList))

# Test run
x, y = 0, 1
print(sum(filterNotEven(fibonacci(x, y, STOP))))