def max_non_intersecting_segments():
    n = int(input().strip())

    segments = []

    for _ in range(n):
        a, b = map(int, input().split())
        segments.append((a, b))

    segments.sort(key=lambda x: x[1])

    count = 0
    end = -1

    for a, b in segments:
        if a > end:
            count += 1
            end = b

    print(count)


max_non_intersecting_segments()
