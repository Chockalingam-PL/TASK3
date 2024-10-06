list = [10,501,22,37,100,999,87,351]

l = len(list)
for i in range(0,l):
    c=0
    for j in range(2,list[i]):
        if list[i] % j == 0:
             c=1
             print(list[i], "is not prime number")
             break
    if c == 0:
        print(list[i], "is prime number")
    
    
