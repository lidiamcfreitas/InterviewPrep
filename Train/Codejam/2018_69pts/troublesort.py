num_test_cases = int(input())


def main():
    results = []
    for i in range(num_test_cases):
        n = input()
        l = [int(x) for x in input().split(" ")]
        n = int(n)

        result = iteration(n,l)
        results.append(result)

    for i, val in enumerate(results):
        print("Case #{}: {}".format(i+1, val))


def iteration(n, p):
    l_odds = []
    l_evens = []
    l_sorted = sorted(p)

    for i, elem in enumerate(p):
        if i % 2 == 0:
            l_evens += [elem]
        else:
            l_odds += [elem]

    l_evens = sorted(l_evens)
    l_odds = sorted(l_odds)

    for i, elem in enumerate(l_sorted):
        if i % 2 == 0 and elem != l_evens[i // 2]:
            return i
        if i % 2 == 1 and elem != l_odds[i // 2]:
            return i

    return "OK"


main()


"""
2
5
5 6 8 4 3
3
8 9 7
"""
"""
Case #1: OK
Case #2: 1
"""