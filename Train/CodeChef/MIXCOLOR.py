import math


def read_input():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = [int(x) for x in input().strip().split()]
        case(N, A)


def case(N, A):
    counter = 0
    max_elem = -math.inf
    s = set()

    for elem in A:
        max_elem = max_elem if elem < max_elem else elem

        if elem in s:
            s.add(elem + max_elem)
            counter += 1
            max_elem = elem + max_elem
        else:
            s.add(elem)

    print(counter)
    return


read_input()