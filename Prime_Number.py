import math as m
def IsPrime(n):
    x=int(m.sqrt(n))
    for i in range(2,x+1):
        if n%i==0:
            return False
    return True
n=int(input())
if IsPrime(n):
    print("Prime")
else:
    print("Not Prime")
