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