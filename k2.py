a=int(input("enter a value for A"))
b=int(input("enter a value for B"))
c=int(input("enter a value for C"))
if(a > b) & (a > c):
    print(a)
elif(b > a) & (b > c):
    print(b)
else:
    print(c)
