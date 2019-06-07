class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = []
        current = 0

        for elem in nums:
            if elem:
                current += 1
            if not elem:
                res += [current]
                current = 0
        res += [current]
        m = max(res)

        for i in range(len(res)-1):
            m = max(m, res[i] + res[i+1] + 1)
        return m
