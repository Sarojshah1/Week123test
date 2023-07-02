# Reverse a string using for loop
a=input("Enter a string")
r=""
i=0
while i<len(a):
    r=a[i]+r
    i=i+1
print("reverse string:",r)