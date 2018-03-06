# general structure
import sys

input_file = ""
output_file = ""
inp = None
out = None


def main():
    global inp, out
    inp = sys.stdin if not input_file else open(input_file, "w+")
    out = sys.stdout if not output_file else open(output_file, "w+")

    read_and_run()

    if inp is not sys.stdin:
        inp.close()
    if out is not sys.stdout:
        out.close()


def read_and_run():

    T = int(inp.input())
    for i in range(T):

        # case specific inputs
        N = int(inp.input())
        A = [int(x) for x in inp.input().strip().split()]

        case(N, A)


def case(N, A):
    global inp, out

    result = 0

    out.write(result)
    return


main()
