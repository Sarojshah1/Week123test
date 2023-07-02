# program to check given number is Armstrong or not
a=int(input("enter a number:"))
b=str(a)
c=0
temp=a
for i in b:
    c=c+int(i)**len(b)
if c==temp:
    print(temp," is a armstrong number")
else:
    print(temp,"is not a armstrong number")