# Knapsack
class Item:
    def __init__(self, height, value):
        self.height = height
        self.value = value


def knapsack(ks_first, ks_second):
    n = len(ks_first)
    K = [[0 for w in range(ks_second + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for w in range(ks_second + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif ks_first[i - 1].height <= w:
                K[i][w] = max(ks_first[i - 1].value + K[i - 1][w - ks_first[i - 1].height], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][ks_second]


items = [Item(10, 60), Item(20, 100), Item(30, 120)]
max_ks = 50
print(knapsack(items, max_ks))


# Binpacking
def binpacking(bp_first, bp_second):
    bp_first.sort(reverse=True)
    bins = []
    for weight in bp_first:
        for i, binpack in enumerate(bins):
            if binpack + weight <= bp_second:
                bins[i] += weight
                break
        else:
            bins.append(weight)
    return len(bins)


array = [2, 5, 4, 7, 1, 3, 8]
max_bp = 10
print(binpacking(array, max_bp))
