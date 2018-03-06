# input:
#  value v
#  sequence a
# output:
#  index i such that a[i]= v or NIL


def linear_search_pretty(a, v):
    for i, elem in enumerate(a):
        if elem == v:
            return i
    return "NIL"


def linear_search(a, v):
    i = 0
    while i < len(a):
        if a[i] == v:
            return i
        else:
            i += 1
    return "NIL"


def main():
    v = int(input())
    a = [int(x) for x in input().strip().split()]

    res = linear_search(a, v)
    print(res)

    return


if __name__ == "__main__":
    main()