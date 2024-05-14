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