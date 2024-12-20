def prime(n):
    if n==1:
        return "! is neither prime nor composite"
    for i in range (2,n):
        if n%i==0:
            return f'{n} is not prime'
    return f'{n} is prime'
n=int(input())
print(prime(n))
