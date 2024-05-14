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