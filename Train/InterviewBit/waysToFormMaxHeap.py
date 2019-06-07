import functools
import math


class Solution:
    # @param n : integer
    # @return an integer
    def solve(self, n):

        def solve_aux(A):

            if A == 2 or A == 1:
                return 1
            if A == 3:
                return 2

            levels_completed = int(math.log(A, 2))
            n = 2 ** levels_completed
            n_div = n / 2
            n_mul = n * 2
            if n/2 == A:
                left = int((A - 1) / 2)
                right = left
            else:
                full_last_line = n
                last_level_values = full_last_line - (n_mul - 1 - A)
                to_add = min(n_div, last_level_values)
                left = to_add + n_div - 1
                right = n_div - 1 + max(0, last_level_values - n_div)

            # print(levels, left, combination(A-1, left), right, combination(A-1, right))
            return combination(A - 1, left) * self.solve(left) * self.solve(right)

        return int(solve_aux(n)) % 1000000007


def memoize(func):
    cache = func.cache = {}
    @functools.wraps(func)
    def memoized_func(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return memoized_func


@memoize
def combination(n, p):
    return math.factorial(n) / (math.factorial(n - p) * math.factorial(p))


s = Solution()
print(s.solve(20))
