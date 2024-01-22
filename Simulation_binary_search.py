import sys

lines = sys.stdin.read().splitlines()
n = int(lines[0])
sequence = set(map(int, lines[1].split()))

for query in lines[2:]:
    if query == '#':
        break
    _, k = query.split()
    k = int(k)
    if k in sequence:
        print(1)
    else:
        print(0)

