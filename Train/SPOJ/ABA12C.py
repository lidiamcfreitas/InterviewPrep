import math
from sys import stdin

num_test_cases = int(input())



def main():
    results = []
    for i in range(num_test_cases):
        n, k = [int(x) for x in input().split(" ")]
        prices = [int(x) for x in input().split(" ")]

        result = iteration(n, k, prices)
        if result == math.inf:
            results.append(-1)
        else:
            results.append(result)

    for val in results:
        print(val)


def iteration(n, k, prices):
    memo = {}

    def m(i, k, n):
        res = None
        if (i, k, n) in memo:
            return memo[(i, k, n)]
        else:
            if i == 0 and k == 0:
                res = 0
            elif i == 0 and k > 0:
                res = math.inf
            else:
                if prices[i - 1] == -1 or k - i < 0 or n == 0:
                    res = m(i - 1, k, n)
                else:
                    res = min(m(i - 1, k, n), m(i - 1, k - i, n - 1) + prices[i - 1])
            if res == None:
                print("Error")
                return
            memo[(i, k, n)] = res
            return res

    return m(k, k, n)


main()

"""
3
3 5
-1 -1 4 5 -1
5 5
1 2 3 4 5
3 8
-1 1 3 -1 5 6 -1 -1

"""

"""
7
3 5
-1 -1 4 5 -1
5 5
1 2 3 4 5
4 6
1 3 -1 -1 -1 -1
3 5
100 40 1 1 2
3 4
1 3 -1 -1
4 5
2 -1 -1 -1 -1
3 5
-1 -1 4 5 -1

"""
