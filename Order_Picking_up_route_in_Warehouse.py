import sys
from itertools import combinations


def solve(N, M, Q, d, q):
    INF = float('inf')
    dp = [[INF] * (1 << N) for _ in range(M + 1)]
    dp[0][0] = 0
    precalc = [[0] * M for _ in range(1 << N)]
    for mask in range(1, 1 << N):
        for shelf in range(M):
            for product in range(N):
                if mask & (1 << product):
                    precalc[mask][shelf] += Q[product][shelf]
    for mask in range(1, 1 << N):
        for shelf in range(M):
            if precalc[mask][shelf] >= q[mask.bit_count() - 1]:
                dp[shelf][mask] = min(dp[shelf][mask], 2 * d[0][shelf])
    for shelf in range(M):
        for mask in range(1, 1 << N):
            dp[shelf][mask] = min(dp[shelf][mask], dp[shelf - 1][mask] + d[0][shelf])
            for submask in range(mask):
                if dp[shelf - 1][submask] + d[0][shelf - 1] + d[shelf - 1][shelf] + d[shelf][0] <= dp[shelf][mask]:
                    dp[shelf][mask] = dp[shelf - 1][submask] + d[0][shelf - 1] + d[shelf - 1][shelf] + d[shelf][0]
                    dp[shelf][mask] = min(dp[shelf][mask],
                                          dp[shelf - 1][mask ^ submask] + d[0][shelf - 1] + d[shelf - 1][shelf] +
                                          d[shelf][0])
    return dp[M - 1][(1 << N) - 1]


N, M = map(int, input().split())
Q = [list(map(int, input().split())) for _ in range(N)]
d = [list(map(int, input().split())) for _ in range(M + 1)]
q = list(map(int, input().split()))
print(solve(N, M, Q, d, q))
