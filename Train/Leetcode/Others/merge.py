'''
Statistics:
Time to solve: quick
# Incorrect attempts: 0
# Hints: 0
# Mistakes: None
# Complexity: O(n*log(n)) maybe possible in O(n) ?
'''


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def in_interval(interval, k):
    start, end = interval
    return start <= k <= end


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        res = []

        if not intervals or len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x: x.start)

        left, right = intervals[0].start, intervals[0].end

        for p in intervals[1:]:
            if in_interval((left, right), p.start):
                right = max(right, p.end)
            else:
                res += [Interval(left, right)]
                left, right = p.start, p.end

        res += [Interval(left, right)]
        return res
