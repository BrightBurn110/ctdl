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