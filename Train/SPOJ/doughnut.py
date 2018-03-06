def problem():
    t = int(input())
    for i in range(t):
        case()


def case():
    c, k, w = [int(x) for x in input().split(" ")]

    print("yes" if c*w <= k else "no")
    return

if __name__ == "__main__":
    problem()