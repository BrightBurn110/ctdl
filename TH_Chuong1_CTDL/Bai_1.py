    ### Cach 1
def fibonacci(n):
    if n < 0:
        return -1
    elif (n == 0) or (n == 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Nhap vao so nguyen n: "))
sb = ""
for i in  range (0, n):
    sb = sb + str(fibonacci(i))
    if i != n - 1:
        sb += ", "
print("Day so fibonacci", n, "la:", sb)

    ### Cach 2
def fibonacci(n):
    f0 = 0
    f1 = 1
    fn = 1
    if n < 0:
        return -1
    elif n == 0 or n == 1:
        return n
    else:
        for i in range (2, n):
            f0 = f1
            f1 = fn
            fn = f0 + f1
        return fn
n = int(input("Nhap vao so nguyen n: "))
sb = ""
for i in  range (0, n):
    sb = sb + str(fibonacci(i))
    if i != n - 1:
        sb += ", "
print("Day so fibonacci", n, "la:", sb)