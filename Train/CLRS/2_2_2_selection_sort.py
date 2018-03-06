# input array


def selection_sort(a):
    for i in range(len(a)-1):
        key = a[i]
        min_v = key
        min_i = i
        for j in range(i+1, len(a)):
            if a[j] < min_v:
                min_i = j
                min_v = a[j]

        a[i] = a[min_i]
        a[min_i] = key

    return a


def main():
    a = [int(_) for _ in input().strip().split()]

    res = selection_sort(a)
    print(res)


if __name__ == '__main__':
    main()
