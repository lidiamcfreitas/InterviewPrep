import math


def main():
    array = [int(_) for _ in input().strip().split()]

    res = merge_sort(array)
    print(res)


def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        mid = len(array) // 2
        if mid:
            left = merge_sort(array[:mid])
            right = merge_sort(array[mid:])
            return merge(left, right)


def merge(a, b):
    i = 0
    j = 0
    a = a + [math.inf]
    b = b + [math.inf]
    res = []
    while i < len(a)-1 or j < len(b)-1:
        if a[i] < b[j]:
            res += [a[i]]
            i += 1
        else:
            res += [b[j]]
            j += 1
    return res


if __name__ == '__main__':
    main()
