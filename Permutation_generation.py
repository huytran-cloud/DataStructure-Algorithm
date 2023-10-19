def print_list(lst):
    output = " ".join(str(x) for x in lst)
    output += " "
    print(output)


def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


def reverse(lst, start, end):
    while start < end:
        swap(lst, start, end)
        start += 1
        end -= 1


def generate_permutations(n):
    lst = list(range(1, n + 1))
    print_list(lst)
    while True:
        i = n - 2
        while i >= 0 and lst[i] >= lst[i + 1]:
            i -= 1
        if i == -1:
            break
        j = n - 1
        while j > i and lst[i] >= lst[j]:
            j -= 1
        swap(lst, i, j)
        reverse(lst, i + 1, n - 1)
        print_list(lst)


n = int(input())
generate_permutations(n)
