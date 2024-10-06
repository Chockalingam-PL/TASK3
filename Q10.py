list = [4, 2, -3, 1, 6]

def sublist(list, l):
    for i in range(l - 1):
        s = list[i]
        for j in range(i + 1, l):
            s += list[j]
            if s == 0:
                return True
    return False

print(sublist(list, len(list)))