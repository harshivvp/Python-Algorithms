def fib_iter(n):

    a,b = 0,1

    for i in range(n):
        a,b = b,a+b

    return a

print(fib_iter(10))