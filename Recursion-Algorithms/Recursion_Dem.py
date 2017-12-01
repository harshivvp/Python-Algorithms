def fact(n):

    #Base Case
    if n == 0:
        return 1

    else:
        return n * fact(n-1)

print("Factorial of number is : ", fact(6))

def fact_add(n):

    if n == 0:
        return 1

    else:
        return (n + fact(n-1))

print("Additional Factorial : ", fact_add(6))

def sum_fact_add(n):

    if len(str(n)) == 1:
        return n
    else:
        return n%10 + sum_fact_add(n/10)

print("Additional Factorial : ", sum_fact_add(321))
