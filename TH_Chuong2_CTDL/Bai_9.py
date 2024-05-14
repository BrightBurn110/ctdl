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