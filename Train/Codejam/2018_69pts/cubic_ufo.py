import math

num_test_cases = int(input())


def main():
    results = []
    for i in range(num_test_cases):
        area = float(input())

        results.append(iteration(area))
    for i, val in enumerate(results):
        x, y, z = val

        x = ' '.join([str(_) for _ in x])
        y = ' '.join([str(_) for _ in y])
        z = ' '.join([str(_) for _ in z])
        print("Case #{}:\n{}\n{}\n{}".format(i+1, x, y, z))


def iteration(area):

    theta_rad = math.pi/4 - math.acos(area / (math.sqrt(2)))

    x = (0.5 * math.sin(theta_rad), 0.5*math.cos(theta_rad), 0)
    y = (x[1], -1 * x[0], 0)
    z = (0, 0, 0.5)     # change for testcase 2

    return x, y, z


main()

'''
2
1.000000
1.414213
'''

'''
Case #1:
0.5 0 0
0 0.5 0
0 0 0.5
Case #2:
0.3535533905932738 0.3535533905932738 0
-0.3535533905932738 0.3535533905932738 0
0 0 0.5
'''