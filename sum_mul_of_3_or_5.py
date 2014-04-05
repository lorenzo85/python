# Find the sum of the multiples of 3 or 5 from 0 to LIMIT
LIMIT = 1000

def multiples() :
    return filter(lambda x : not x%3 or not x%5, range(0, LIMIT + 1))

print(sum(multiples()))