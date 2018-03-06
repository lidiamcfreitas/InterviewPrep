import math


def case(a):
    s = a[:]
    for i in range(1, len(a)):
        s[i] += s[i-1]

    last_i = len(a) - 1
    res = [0] * len(a)

    s_v = [-math.inf]+[s[i] + a[i] for i in range(1, len(a))]

    z = list(zip([i for i in range(len(a))], s_v))

    z = sorted(z, key=lambda x: x[1])

    print(z)

    for i in range(last_i):
        e_i = z[i][0]
        e_s = s[e_i]

        lo = i + 1
        hi = last_i

        while lo < hi:
            mid = lo + (hi - lo)//2

            if e_s < z[mid][1]:
                hi = mid
            else:
                lo = mid + 1

        if e_s < z[lo][1]:
            res[e_i] = lo - 1 - i
        else:
            res[e_i] = lo - i

    print(res)


def main():
    t = int(input())

    for _ in range(t):
        _ = input()
        a = [int(x) for x in input().strip().split()]

        case(a)


main()
