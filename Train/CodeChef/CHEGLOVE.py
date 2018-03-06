
def read_input():
    T = int(input())
    for i in range(T):
        N = int(input())
        L = [int(x) for x in input().strip().split()]
        G = [int(x) for x in input().strip().split()]

        case(N,L,G)


def case(N,L,G):
    possible = ["front", "back"]

    for i in range(N):
        if not possible:
            print("none")
            return

        if L[i] > G[i] and "front" in possible:
            possible.remove("front")

        if L[i] > G[-(i+1)] and "back" in possible:
            possible.remove("back")
    if len(possible) == 1:
        print(possible[0])
    elif not possible:
        print("none")
    else:
        print("both")
    return

read_input()