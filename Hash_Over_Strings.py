def compute_hash(s, m):
    hash_value = 0
    p = 256  # base
    p_pow = 1
    for c in reversed(s):
        hash_value = (hash_value + ord(c) * p_pow) % m
        p_pow = (p_pow * p) % m
    return hash_value

n, m = map(int, input().split())
for _ in range(n):
    s = input().strip()
    print(compute_hash(s, m))
