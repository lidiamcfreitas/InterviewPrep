# INPUT
#  2 n-bit arrays
# OUTPUT
#  1 (n+1)-bit array


def binary_sum(a, b):
    res = ""
    over = 0
    for i in range(len(a)):
        sum = a[i] + b[i] + over

        if sum == 0:
            res = "0" + res
            over = 0
        elif sum == 1:
            res = "1" + res
            over = 0
        elif sum == 2:
            res = "0" + res
            over = 1
        elif sum == 3:
            res = "1" + res
            over = 1

    if over == 1:
        res = "1" + res
    else:
        res = "0" + res

    return res


def main():
    a = [int(x) for x in str(input())]
    b = [int(x) for x in str(input())]

    res = binary_sum(a, b)
    print(res)


main()