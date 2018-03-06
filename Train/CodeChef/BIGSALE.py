
def read_input():
    T = int(input())
    for i in range(T):
        N = int(input())
        case(N)


def case(N):
    loss = 0
    for i in range(N):
        P, Q, D = [int(x) for x in input().strip().split()]
        D /= 100
        loss += Q * ( P - ( P * (1 + D) * (1 - D)))
    print(loss)

read_input()