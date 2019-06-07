from time import time


# Example input
'''
7
1 3 5 7 0 3 4
'''


def sum2_equals_k_hash(array, k):     # amortized O(n)
    start_t = time()
    d = {}
    res = set()

    for elem in array:
        complement = k - elem
        if elem not in d:
            d[elem] = 1
        if complement in d:
            res.add((elem, complement))
            res.add((complement, elem))

    print("sum2_equals_k_hash \ntime:{:.2} seconds\tres:{}".format(time()-start_t, res))
    return res


def sum2_equals_k_binary_search(array, k):     # n log(n)
    start_t = time()
    array = sorted(array)
    res = set()

    def exists(c):
        lo = 0
        hi = len(array)-1
        while lo < hi:
            mid = lo + (hi - lo)//2
            if array[mid] >= c:
                hi = mid
            else:
                lo = mid + 1

        return array[lo] == c

    for elem in array:
        complement = k - elem

        if exists(complement):
            res.add((elem, complement))

    print("sum2_equals_k_binary_search \ntime:{:.2} seconds\tres:{}".format(time() - start_t, res))
    return res


def main():
    k = int(input())
    a = [int(_) for _ in input().strip().split(" ")]

    sum2_equals_k_hash(a, k)
    sum2_equals_k_binary_search(a, k)


if __name__ == '__main__':
    main()
