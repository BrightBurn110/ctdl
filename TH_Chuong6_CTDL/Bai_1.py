def duyNhat(a):
    a.sort()
    b = []
    for i in range(len(a)):
        if i == 0 or a[i] != a[i - 1]:
            b.append(a[i])
    return b

#Ex:
a = [1, 5, 3, 7, 5, 9, 7]
print(duyNhat(a))