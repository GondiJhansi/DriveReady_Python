#program to print 1 to 10
for i in range(1,11):
    print(i)

def display(x):
    if x>10:
        return
    print(x)
    display(x+1)
display(1)
    
