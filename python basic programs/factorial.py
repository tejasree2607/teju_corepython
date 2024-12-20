def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
n=int(input("enter any number"))
print(fact(n))