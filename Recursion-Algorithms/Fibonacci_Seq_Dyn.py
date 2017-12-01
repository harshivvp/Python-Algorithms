n = 12
cache = [None] * (n + 1)

def fib_dyn(n):

    #Base case:
    if n == 1 or n == 0:
        return n

    #Check cache:
    if cache[n] != None:
        return cache[n]

    #Keep setting the cache:

    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
    return cache[n]

print(fib_dyn(12))

