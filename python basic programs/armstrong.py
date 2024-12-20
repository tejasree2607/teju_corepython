def armstrong(n):
    a=n
    res=0
    while n>0:
        r=n%10
        res+=r**3
        n=n//10
        
    if a==res:
        return "it is armstrong"
    return " it is not armstrong"
n=int(input())
print(armstrong(n))