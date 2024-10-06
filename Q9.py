list = [10,20,30,9]

def triplets(list, n):
    for i in range(n-1):
        s=set()
        for j in range(i+1, n):
            x =-(list[i]+list[j])
            if x in s:
                print(l,list[i],list[j])
                found = True
