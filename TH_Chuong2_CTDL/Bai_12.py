def Cong(a, b):
    num_a = int(''.join(map(str, a[1:])))
    num_b = int(''.join(map(str, b[1:])))
    sign_result = 0 if a[0] == b[0] else 1
    if sign_result == 0:
        result = num_a + num_b
    else:
        result = num_a - num_b
    max_value = 10 ** (len(a) - 1) - 1
    if abs(result) > max_value:
        return [-1] * (len(a) - 1)
    else:
        if sign_result == 0:
            return [0] + list(map(int, str(abs(result))))
        else:
            return [1] + list(map(int, str(abs(result))))
if __name__ == "__main__":
    a = [0, 1, 2, 3]
    b = [1, 0, 9, 8, 7]

    print("Result of a + b:", Cong(a, b))