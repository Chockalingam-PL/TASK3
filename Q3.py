n=int(input("enter the of input "))
x=n
while x>=10:
    sum=0
    while x>0:
        r=x%10
        sum=sum+(r**2)
        x=x//10
    x=sum
if(x==1):
    print(n," is happy number")
else:
    print(n," is not happy number")