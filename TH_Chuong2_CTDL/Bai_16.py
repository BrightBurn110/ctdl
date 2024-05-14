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