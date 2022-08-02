#program to print 10 to 1

def display(x):
    if x<1:
        return
    print(x)
    display(x-1)
display(10)
