import sys

num_test_cases = int(input())


def main():

    def play(i,j):
        print("{} {}".format(i, j), file=sys.stdout)
        sys.stdout.flush()

        # print("play: {} {}".format(i, j), file=sys.stderr)
        # sys.stderr.flush()

    for test_case in range(num_test_cases):
        field = set()
        a = int(input())

        # print("starting with a =", a, file=sys.stderr)
        # sys.stderr.flush()

        squares = {}
        squares_limit = (a - 1) // 3 + 1

        for i in range(10):
            squares[i] = set()

        for i in range(2, squares_limit):
            squares[9].add(i)

        i, j = 2, 2

        play(i, j)
        success = False

        while i > 0 and j > 0:
            i, j = [int(_) for _ in input().strip().split(' ')]
            if i == 0 and j == 0:
                success = True
                break
            if i == -1 and j == -1:
                break

            # print("read: {} {}".format(i, j), file=sys.stderr)
            # sys.stderr.flush()

            if (i, j) in field:  # miss!
                # print('miss!', file=sys.stderr)
                sys.stderr.flush()

                play(i_play, 2)  # keep same tactic
            else:   # hit
                field.add((i, j))

                for i_new in (i - 1, i, i + 1):
                    if i_new < 2 or i_new > squares_limit:
                        continue
                    updated = False
                    squares_i = 9
                    while not updated and squares_i:
                        if i_new not in squares[squares_i]:
                            squares_i -= 1
                        else:
                            squares[squares_i].remove(i_new)
                            squares[squares_i-1].add(i_new)
                            updated = True

                squares_i = 9
                while not squares[squares_i]:
                    squares_i -= 1

                # print(squares, file=sys.stderr)
                # sys.stderr.flush()

                i_play = squares[squares_i].pop()
                play(i_play, 2)
                squares[squares_i].add(i_play)

        if success:
            print("wowowowow! Passed testcase #{}".format(test_case), file=sys.stderr)
            sys.stderr.flush()

main()
