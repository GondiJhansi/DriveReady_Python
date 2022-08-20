n=int(input("Enter number of students:"))
d={}
for i in range(n):
    name=input("Enter Student Name:")
    marks=int(input("Enter Student Marks:"))
    d[name]=marks
print("Al students data inserted")
while True:
    name=input("Enter Student name to get marks:")
    if name in d:
        print("The marks of {}:{}".format(name,d.get(name)))
    else:
        print("Student not found")
    option=input("Do you want to find another student marks [Yes|No]:")
    while option.lower() not in ['yes','no']:
        option=input("Invalid option,please choose valid option [Yes|No]:")
    if option.lower()=='no':
        break
print("Thanks for using our application")   
    
