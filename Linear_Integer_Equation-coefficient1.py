def huytransieudeptrai(n, M, collection, count):
    if n == 0:
        if M == 0:
            print(' '.join(str(num) for num in collection), end=' ')
            count += 1
            if count < 3:
                print()
        return

    for i in range(1, M + 1):
        if i <= M:
            huytransieudeptrai(n - 1, M - i, collection + [i], count)


n, M = map(int, input().split())

count = 0
huytransieudeptrai(n, M, [], count)