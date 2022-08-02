def digcount(n):
    if n==0:
        return 0
    return 1+digcount(n//10)
print(digcount(1234))
