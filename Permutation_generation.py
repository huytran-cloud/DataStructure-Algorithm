def generate_permutations(n):
    nums = list(range(1, n + 1))
    def swap(nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def reverse(nums, start):
        i = start
        j = len(nums) - 1
        while i < j:
            swap(nums, i, j)
            i += 1
            j -= 1

    result = []
    result.append(" ".join(map(str, nums)))

    while True:
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i == -1:
            break

        j = n - 1
        while nums[i] >= nums[j]:
            j -= 1

        swap(nums, i, j)

        reverse(nums, i + 1)

        result.append(" ".join(map(str, nums)))

    return result


n = int(input("Enter an integer: "))
permutations = generate_permutations(n)
for permutation in permutations:
    print(permutation)
