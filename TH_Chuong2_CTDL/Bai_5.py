def Cong(a, b):
    num_a = int(''.join(map(str, a)))
    num_b = int(''.join(map(str, b)))
    result = num_a + num_b
    max_value = 10 ** len(a) - 1
    if result > max_value:
        return [-1] * len(a)
    else:
        return list(map(int, str(result)))
if __name__ == "__main__":
    a = [1, 2, 3]
    b = [9, 8, 7]

    print("Result of a + b:", Cong(a, b))