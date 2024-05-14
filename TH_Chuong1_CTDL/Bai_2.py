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