n=int(input())
c=0
while n:
    r=n%10
    n=n//10
    if r%2==0:
        c+=1
print(c)
