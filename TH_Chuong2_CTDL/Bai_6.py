def Tru(a, b):
    num_a = int(''.join(map(str, a)))
    num_b = int(''.join(map(str, b)))
    result = num_a - num_b
    
    return result
if __name__ == "__main__":
    a = [7, 8, 9]
    b = [1, 2, 3]

    print("Result of a - b:", Tru(a, b))