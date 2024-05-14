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