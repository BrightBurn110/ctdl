def Hieu(a, b):
    a.sort()
    b.sort()
    c = []
    for num in a:
        if num not in b:
            c.append(num)
    return c

#Ex:
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
print(Hieu(a, b))