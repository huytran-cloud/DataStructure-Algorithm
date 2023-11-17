n = int(input())
distances = [list(map(int, input().split())) for _ in range(n)]

dp = [[float('inf')] * n for _ in range(1 << n)]
dp[1][0] = 0
for mask in range(1, 1 << n):
    for city in range(n):
        if mask & (1 << city) == 0:
            continue
        for last_city in range(n):
            if mask & (1 << last_city) == 0:
                continue
            prev_mask = mask ^ (1 << city)
            dp[mask][city] = min(dp[mask][city], dp[prev_mask][last_city] + distances[last_city][city])

min_distance = float('inf')

for city in range(n):
    min_distance = min(min_distance, dp[(1 << n) - 1][city] + distances[city][0])

print(min_distance)