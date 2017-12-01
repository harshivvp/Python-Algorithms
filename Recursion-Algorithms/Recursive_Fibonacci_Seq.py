def fib_rec(n):

    #Base case
    if n == 0 or n == 1:
        return n

    #Recursive Case
    else:
        value = fib_rec(n-1) + fib_rec(n-2)
        return value

print(fib_rec(10))