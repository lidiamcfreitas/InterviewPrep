import math


def main():
    T = int(input())

    for t in range(T):
        N, H = [int(_) for _ in input().strip().split()]
        A = [int(_) for _ in input().strip().split()]

        case(N, H, A)


def case(N, H, A):
    # first sort the array -      a log(a)
    A = sorted(A)

    def value(pos_i, div):           # n
        if pos_i == len(A) - 1:
            return len(A)
        return pos_i + 1 + sum([math.ceil(_ / div) for _ in A[pos_i + 1:]])

    def predicate(pos_i):
        return value(pos_i, A[pos_i]) <= H

    def predicate_2(pos_i, div):
        return value(pos_i, div) <= H

    # second do binary search on the array to find the lowest K that satisfies the predicate
    lo = 0
    hi = len(A) - 1

    while lo < hi:              # log a
        mid = lo + int((hi - lo)/2)

        if predicate(mid):
            hi = mid
        else:
            lo = mid + 1

    # third part, binary search in between the chosen and the previous, but outside array

    #if value(lo, A[lo]) == H:
    #    print(A[lo])
    #    return A[lo]
    #else:

    if  lo:
        res_1 = lo
        lo = A[res_1-1]
    else:
        res_1 = 0
        #if len(A) == 1:
        #    predicate_2 = lambda x, y : math.ceil(A[0] / y) <= H
        lo = math.ceil(A[0] / H)
    hi = A[res_1]
    res = None
    while lo < hi:
        res = lo + int((hi - lo)/2)

        if predicate_2(res_1 - 1, res):
            hi = res
        else:
            lo = res + 1

    if res is None:
        raise  "error"

    print(lo)
    return lo


if __name__ == "__main__":
    main()




