### Chuong 1
### Bai 1
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

### Bai 2
def neper(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        total = 1
        ak = 1
        for k in range(1, n + 1):
            ak *= 1/k
            total += ak
        return total

n = int(input("Nhap vao so nguyen n: "))
print("Tong cua cac so hang tu a0 den an la:", neper(n))
### Bai 3
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

### Bai 4
def pascal(n):
    if n <= 0:
        print("Không có tam giác Pascal cho n <= 0")
        return

    for i in range(n + 1):
        print("n=" + str(i), end=" ")
        for j in range(i + 1):
            print(combination(i, j), end=" ")
        print()

def combination(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return combination(n - 1, k - 1) + combination(n - 1, k)

n = int(input("Nhập vào số nguyên dương n: "))
pascal(n)

### Bai 5
def number(x, y):
    for n in range(x, y + 1):
        divisor_sum = sum_of_divisors(n)
        if divisor_sum < n:
            print(n, "là deficient.")
        elif divisor_sum == n:
            print(n, "là perfect.")
        else:
            print(n, "là abundant.")

def sum_of_divisors(n):
    divisor_sum = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            other_divisor = n // i
            if other_divisor != i:
                divisor_sum += other_divisor
    return divisor_sum

x = int(input("Nhập vào số nguyên dương x: "))
y = int(input("Nhập vào số nguyên dương y (x ≤ y): "))
number(x, y)
