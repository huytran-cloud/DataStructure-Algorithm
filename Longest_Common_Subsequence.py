import sys


def lcs(x, y):
    n = len(x)
    m = len(y)

    table = [0] * (m + 1)

    for i in range(1, n + 1):
        prev = 0
        for j in range(1, m + 1):
            current = table[j]
            if x[i - 1] == y[j - 1]:
                table[j] = prev + 1
            else:
                table[j] = max(table[j - 1], table[j])
            prev = current

    result = table[m]

    return result


n, m = map(int, sys.stdin.readline().split())
x = list(map(int, sys.stdin.readline().split()))
y = list(map(int, sys.stdin.readline().split()))
sys.stdout.write(str(lcs(x, y)))
