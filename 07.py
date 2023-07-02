# Python program to count the space of a given string
a=input("enter a string")
d=0
for i in a:
    if i.isspace():
        d=d+1
print("total space =",d)