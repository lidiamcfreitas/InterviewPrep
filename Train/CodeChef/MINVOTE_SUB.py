
def case(a):
    sum_a = a[:]
    for i in range(1, len(a)):
        sum_a[i] += sum_a[ i -1]

    last_i = len(a) -1
    res = [0] * len(a)

    for elem_i, elem_v in enumerate(a):
        if elem_i != last_i:  # to the right
            lo = elem_i + 1
            hi = last_i

            while lo < hi:
                mid = lo + (hi - lo) // 2
                dist = sum_a[mid - 1] - sum_a[elem_i]
                if dist > elem_v:
                    hi = mid
                else:
                    lo = mid + 1

            for i in range(elem_i + 1, lo):
                res[i] += 1

            if sum_a[lo - 1] - sum_a[elem_i] <= elem_v:
                res[lo] += 1

        if elem_i:  # to the left
            lo = 0
            hi = elem_i - 1

            while lo < hi:
                mid = lo + (hi - lo) // 2
                dist = sum_a[elem_i - 1] - sum_a[mid]
                if dist <= elem_v:
                    hi = mid
                else:
                    lo = mid + 1
            if sum_a[elem_i - 1] - sum_a[lo] <= elem_v:
                for i in range(lo, elem_i):
                    res[i] += 1

    print(' '.join([str(_) for _ in res]))


def main():
    t = int(input())

    for _ in range(t):
        _ = input()
        a = [int(x) for x in input().strip().split()]

        case(a)


main()
