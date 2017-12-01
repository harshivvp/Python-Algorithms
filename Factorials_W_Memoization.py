#create cache for known results

factorial_memo = {}

def factorial(f):

    if f < 2:
        return 1

    if not f in factorial_memo:
        factorial_memo[f] = f * factorial(f-1)

    return factorial_memo[f]

print(factorial(4))