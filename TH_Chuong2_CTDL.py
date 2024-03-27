### Bai 1
def DoiXung(matrix):
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            return False
        
    for i in range(n):
        for j in range(i):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

if __name__ == "__main__":
    matrix1 = [[1,2,3], [2,9,6], [3,5,6]]
    matrix2 = [[1,2,3], [2,4,5], [3,5,6]]
    
    print("Matrix 1 is symmetric:", DoiXung(matrix1))
    print("Matrix 2 is symmetric:", DoiXung(matrix2))

### Bai 2
def TamGiacTren(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            if matrix[i][j] != 0:
                return False
    return True

if __name__ == "__main__":
    matrix1 = [[1, 2, 3], [0, 4, 5], [0, 0, 6]]
    matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print("Matrix 1 is upper triangular:", TamGiacTren(matrix1))
    print("Matrix 2 is upper triangular:", TamGiacTren(matrix2))

### Bai 3
def TrungHang(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i] == matrix[j]:
                return True

    return False
if __name__ == "__main__":
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[1, 2, 3], [4, 5, 6], [1, 2, 3]]
    matrix3 = [[1, 2, 3], [4, 5, 6], [4, 5, 6]]

    print("Matrix 1 has at least two identical rows:", TrungHang(matrix1))
    print("Matrix 2 has at least two identical rows:", TrungHang(matrix2))
    print("Matrix 3 has at least two identical rows:", TrungHang(matrix3))

### Bai 4
def NhomHang(matrix):
    n = len(matrix)
    grouped_rows = []
    for i in range(n):
        found = False
        for group in grouped_rows:
            if matrix[i] in group:
                found = True
                break
        if not found:
            new_group = [matrix[i]]
            for j in range(i + 1, n):
                if matrix[i] == matrix[j]:
                    new_group.append(matrix[j])
            grouped_rows.append(new_group)
    for group in grouped_rows:
        print("Group:")
        for row in group:
            print(row)
if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [1, 2, 3], [7, 8, 9], [4, 5, 6], [10, 11, 12], [7, 8, 9]]

    NhomHang(matrix)

### Bai 5
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

### Bai 6
def Tru(a, b):
    num_a = int(''.join(map(str, a)))
    num_b = int(''.join(map(str, b)))
    result = num_a - num_b
    
    return result
if __name__ == "__main__":
    a = [7, 8, 9]
    b = [1, 2, 3]

    print("Result of a - b:", Tru(a, b))

### Bai 7
def Nhan(a, b):
    num_a = int(''.join(map(str, a)))
    num_b = int(''.join(map(str, b)))
    result = num_a * num_b
    max_value = 10 ** len(a) - 1
    if result > max_value:
        return [-1] * len(a)
    else:
        return list(map(int, str(result)))
if __name__ == "__main__":
    a = [1, 2, 3]
    b = [9, 8, 7]

    print("Result of a * b:", Nhan(a, b))

### Bai 8
def TamGiacDuoi(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != 0:
                return False

    return True
if __name__ == "__main__":
    matrix1 = [[1, 0, 0], [2, 3, 0], [4, 5, 6]]
    matrix2 = [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
    matrix3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print("Matrix 1 is lower triangular:", TamGiacDuoi(matrix1))
    print("Matrix 2 is lower triangular:", TamGiacDuoi(matrix2))
    print("Matrix 3 is lower triangular:", TamGiacDuoi(matrix3))

### Bai 9
def TrungCot(matrix):
    n = len(matrix)
    cols_set = set(tuple(col) for col in zip(*matrix))
    return len(cols_set) < n
if __name__ == "__main__":
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[1, 2, 1], [4, 5, 4], [7, 8, 7]]
    matrix3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

    print("Matrix 1 has at least two identical columns:", TrungCot(matrix1))
    print("Matrix 2 has at least two identical columns:", TrungCot(matrix2))
    print("Matrix 3 has at least two identical columns:", TrungCot(matrix3))

### Bai 10
def NhomCot(matrix):
    n = len(matrix)
    cols_set = set(tuple(col) for col in zip(*matrix))
    grouped_cols = []
    for col in cols_set:
        group = [i for i, x in enumerate(zip(*matrix)) if x == col]
        grouped_cols.append(group)
    for group in grouped_cols:
        print("Group:")
        for col_index in group:
            print(col_index)
if __name__ == "__main__":
    matrix = [[1, 2, 1], [4, 5, 4], [7, 8, 7], [1, 2, 1]]
    NhomCot(matrix)

### Bai 11
def Tru(a, b):

    num_a = int(''.join(map(str, a[1:])))
    num_b = int(''.join(map(str, b[1:])))
    sign_result = 0 if a[0] == b[0] else 1
    if sign_result == 0:
        result = num_a - num_b
    else:
        result = num_a + num_b
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

    print("Result of a - b:", Tru(a, b))


### Bai 12
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

### Bai 13
def Nhan(a, b):
    num_a = int(''.join(map(str, a[1:])))
    num_b = int(''.join(map(str, b[1:])))
    sign_result = 0 if a[0] == b[0] else 1
    if sign_result == 0:
        result = num_a * num_b
    else:
        result = -(num_a * num_b)
    max_value = 10 ** (len(a) - 1) - 1
    if abs(result) > max_value:
        return [-1] * (len(a) - 1)
    else:
        if sign_result == 0:
            return [0] + list(map(int, str(abs(result))))
        else:
            return [1] + list(map(int, str(abs(result))))
if __name__ == "__main__":
    a = [1, 2, 3]
    b = [1, 0, 9, 8, 7]

    print("Result of a * b:", Nhan(a, b))

### Bai 14
def DayConDauTien(a, b):
    n = len(a)
    m = len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    max_length = 0
    end_index = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i - 1
    start_index = end_index - max_length + 1
    common_subsequence = a[start_index:end_index + 1]

    return common_subsequence
if __name__ == "__main__":
    a = [1, 6, 2, 5, 3, 7, 9, 4, 2]
    b = [9, 6, 2, 5, 3, 7, 8]

    result = DayConDauTien(a, b)
    print("Common subsequence:", result)

### Bai 15
def DayConDaiNhat(a, b):
    n = len(a)
    m = len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    max_length = 0
    end_index = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i - 1
    start_index = end_index - max_length + 1
    common_subsequence = a[start_index:end_index + 1]

    return common_subsequence
if __name__ == "__main__":
    a = [1, 6, 2, 5, 3, 7, 9, 4, 2, 8, 1, 5]
    b = [6, 2, 5, 3, 7, 9, 8, 1, 5]

    result = DayConDaiNhat(a, b)
    print("Longest common subsequence:", result)

### Bai 16
def Dao(matrix):
    n = len(matrix)
    def compute_max_area(x, y):
        area = 0
        queue = [(x, y)]
        while queue:
            i, j = queue.pop(0)
            if 0 <= i < n and 0 <= j < n and matrix[i][j] == 1:
                matrix[i][j] = 0
                area += 1
                queue.append((i + 1, j))
                queue.append((i - 1, j))
                queue.append((i, j + 1))
                queue.append((i, j - 1)) 
        return area

    max_area = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                area = compute_max_area(i, j)
                max_area = max(max_area, area)

    print("Maximum area of rectangular islands:", max_area)
if __name__ == "__main__":
    matrix = [
        [1, 0, 1, 0, 0],
        [1, 0, 0, 1, 1],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 1]
    ]

    Dao(matrix)
