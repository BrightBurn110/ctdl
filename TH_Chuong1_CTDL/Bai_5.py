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