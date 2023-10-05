k, n = map(int, input().split())

def computeCombination(k, n):
    MOD = 10 ** 9 + 7
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    for i in range(k + 1):
        for j in range(n + 1):
            if i == 0 or i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i][j - 1]) % MOD

    return dp[k][n]

combination = computeCombination(k, n)
print(combination)