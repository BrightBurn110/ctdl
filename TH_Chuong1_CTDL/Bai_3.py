    ### Cach 1
def gcb(m, n):
    if n < 0 or m < 0:
        return -1
    elif n == 0:
        return m
    else:
        return gcb(n, m % n)
m = int(input("Nhap vao so nguyen duong m: "))
n = int(input("Nhap vao so nguyen duong n: "))
# print("Uoc chung lon nhat cua", m, "va", n, "la:", gcb(m, n))
    ### Cach 2
def gcb(m, n):
    if n <= 0 or m <= 0:
        return -1
    while n!= 0:
        m, n = n, m % n
    return m
m = int(input("Nhap vao so nguyen duong m: "))
n = int(input("Nhap vao so nguyen duong n: "))
print("Uoc chung lon nhat cua", m, "va", n, "la:", gcb(m, n))