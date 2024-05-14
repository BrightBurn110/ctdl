def Hop(a, b):
    a.sort()
    b.sort()
    c = []
    for num in a:
        if num not in c:
            c.append(num)
    for num in b:
        if num not in c:
            c.append(num)
    c.sort()
    return c

#Ex:
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
print(Hop(a, b))