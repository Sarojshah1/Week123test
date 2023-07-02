# write a program to display integer from of a list. given list=[1,"a","c",2,3,4]
list=[1,"a","c",2,3,4]
l=[]
for i in list:
    if type(i)==int:
        l=l+[i]
print(l)