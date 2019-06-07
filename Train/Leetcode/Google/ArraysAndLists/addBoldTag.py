def in_interval(interval, k):
    start, end = interval
    return start <= k <= end


def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """

    res = []

    if not intervals or len(intervals) == 1:
        return intervals

    intervals.sort(key=lambda x: x[0])

    left, right = intervals[0][0], intervals[0][1]

    for p in intervals[1:]:
        if in_interval((left, right), p[0]):
            right = max(right, p[1])
        else:
            res += [(left, right)]
            left, right = p[0], p[1]

    res += [(left, right)]
    return res

class Solution:
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """

        if not s or not dict:
            return s

        # find pairs
        pairs = []

        for substring in dict:
            found_i = s.find(substring, 0)
            if found_i != -1:
                pairs += [(found_i, found_i + len(substring)-1)]

            while found_i != -1:
                found_i = s.find(substring, found_i+1)
                if found_i != -1:
                    pairs += [(found_i, found_i + len(substring)-1)]

        if not pairs:
            return s

        pairs.sort()

        new_res = merge(pairs)

        str_res = s[:new_res[0][0]]

        for i, p in enumerate(new_res):
            str_res += "<b>" + s[p[0]:p[1]+1] + "</b>"
            if i != len(new_res)-1:
                str_res += s[p[1]+1:new_res[i+1][0]]

        if new_res[-1][1]+1 != len(s):
            str_res += s[new_res[-1][1]+1:]

        return str_res.replace(r"</b><b>", "")


a = Solution()
print(a.addBoldTag("aaabbc", ["aaa", "aab", "bc"]))
print(a.addBoldTag("aaabbcc", ["aaa", "aab", "bc"]))
params = {"s":"abcxyz123" , "dict": ["abc","123"]}
print(a.addBoldTag(**params))
params = {"s":"aaabbcc" , "dict": ["aaa","aab","bc","aaabbcc"]}
print(a.addBoldTag(**params))

params = {"s":"aaabbcc" , "dict": ["a","b","c"]}
print(a.addBoldTag(**params))
