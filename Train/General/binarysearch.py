def main():
    s = int(input())
    A = [int(_) for _ in input().strip().split()]

    print(binary_search(A, s))


def binary_search(A, s):
    # find the smallest value larger than s
    lo, hi = 0, len(A) - 1

    def predicate(x):
        return A[x] >= s

    while lo < hi:
        mid = lo + int((hi - lo)/2)

        if predicate(mid):
            hi = mid
        else:
            lo = mid + 1

    if not predicate(lo):
        raise "there's no value in the array that is larger than s!"

    return lo, A[lo]


if __name__ == "__main__":
    main()

