num_test_cases = int(input())


def main():
    results = []
    for i in range(num_test_cases):
        n, p = [x for x in input().split(" ")]
        n = int(n)

        result = iteration(n, p)
        results.append(result)

    for i, val in enumerate(results):
        print("Case #{}: {}".format(i+1, val))


def iteration(n, p):
    # parse
    damage = 0
    charge = 1
    d_charges = {}
    d_shots = {}
    max_s = -1
    result = 0

    for i, c in enumerate(p):
        if c ==  "C":
            charge *= 2
            d_charges[i] = charge
        if c == "S":
            max_s = i
            damage += charge
            d_shots[i] = charge

    num_shots = len(d_shots)
    if num_shots > n:
        return "IMPOSSIBLE"
    if max_s == -1:
        return 0

    while damage > n:
        right_shot = max_s
        while right_shot - 1 in d_shots:
            right_shot -= 1
        shot_damage = d_shots[right_shot]

        del d_shots[right_shot]
        d_shots[right_shot-1] = shot_damage // 2
        damage -= d_shots[right_shot-1]
        result += 1

    return result


main()

"""
6
1 CS
2 CS
1 SS
6 SCCSSC
2 CC
3 CSCSS

"""

"""
Case #1: 1
Case #2: 0
Case #3: IMPOSSIBLE
Case #4: 2
Case #5: 0
Case #6: 5

"""
