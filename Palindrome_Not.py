n=int(input())
rev=0
temp=n
while n:
    r=n%10
    rev=rev*10+r
    n=n//10
if temp==rev:
    print("Palindrome")
else:
    print("Not Palindrome")
