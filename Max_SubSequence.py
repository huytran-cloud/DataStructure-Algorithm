def highest_weight_subsequence(n, a):
    dp = [0] * n
    dp[0] = a[0]
    for i in range(1, n):
        dp[i] = max(a[i], a[i] + dp[i-1])
    return max(dp)

# Example usage
n = int(input())
a = list(map(int, input().split()))
result = highest_weight_subsequence(n, a)
print(result)