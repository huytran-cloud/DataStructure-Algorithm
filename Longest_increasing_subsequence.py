import bisect


def lis(a):
    d = [1] * n
    for i in range(1, n):
        for j in range(i):
            if a[j] < a[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1

    return max(d)
    # b = []
    # for _ in a:
    #     i = bisect.bisect_left(b, _)
    #     if i == len(b):
    #         b.append(_)
    #     else:
    #         b[i] = _
    #
    # return len(b)


n = int(input())
a = list(map(int, input().split()))

print(lis(a))
