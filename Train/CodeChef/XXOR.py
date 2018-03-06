import numpy as np
import math


def main():
    N, Q = [int(_) for _ in input().strip().split()]
    A = [int(_) for _ in input().strip().split()]

    max_len = - math.inf
    for e in A:
        if e:
            l = int(math.log(e,2)) + 1
        else:
            l = 0
        max_len = l if l > max_len else max_len

    M = np.zeros(((len(A), max_len)))

    for i in range(N):
        x = A[i]
        j = max_len - 1
        while x or j >= 0:
            if not x:
                M[i, j] = M[i - 1, j]
                j -= 1
                continue

            if x % 2:
                if M[i,j] == 0 and i:
                    M[i,j] = M[i-1, j] + 1
                else:
                    M[i,j] += 1
            elif i:
                M[i,j] = M[i-1,j]

            x = x // 2
            j -= 1

    for _ in range(Q):
        res = ''

        L, R = [int(x)-1 for x in input().strip().split()]
        threshold = (R-L+1)/2
        sums = M[R] if not L else M[R] - M[L-1]

        for elem in sums:
            if elem >= threshold:
                res += '1'
            else:
                res += '0'

        result = 2147483648 if not res else 2147483648 - int(res, 2) - 1

        print(result)


if __name__ == "__main__":
    main()
