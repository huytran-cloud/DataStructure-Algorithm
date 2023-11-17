def tsp(n, dist):
    dp = [[-1] * (1 << n) for _ in range(n)]
    def tsp_dp(mask, pos):
        if mask == (1 << n) - 1:
            return dist[pos][0]
        if dp[pos][mask] != -1:
            return dp[pos][mask]

        ans = float('inf')
        for city in range(n):
            if (mask >> city) & 1 == 0:
                ans = min(ans, dist[pos][city] + tsp_dp(mask | (1 << city), city))

        return ans

    return tsp_dp(1, 0)


n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]
print(tsp(n, dist))
