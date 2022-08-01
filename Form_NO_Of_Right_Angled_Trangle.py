import math
n=int(input())
c=0
x=int(math.sqrt(n))
for i in range(1,x+1):
    if n%i==0:
        x=n//i
        if (i!=x and i%2==x%2):
            c+=1
print(c)
