def lcs(x, y):
    n = len(x)
    m = len(y)

    table = [[0 for x in range(m + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    return table[n][m]


n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
print(lcs(x, y))
