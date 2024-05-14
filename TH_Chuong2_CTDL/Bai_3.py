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