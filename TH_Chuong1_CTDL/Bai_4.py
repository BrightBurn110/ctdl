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