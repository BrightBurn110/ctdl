def Giao(a ,b):
    a.sort()
    b.sort()
    c = []
    for num in a:
        if num in b and num not in c:
            c.append(num)
    c = sorted(list(set(c)))
    return c

#Ex:
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
print(Giao(a, b))