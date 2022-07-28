n=int(input())
res=0
while n:
    r=n%10
    res=res+r*r
    n=n//10
    if n==0:
        n=res
        res=0
        if n>=1 and n<=9:
            break
if n==1:
    print("Happy Number")
else:
    print("Not Happy Number")
