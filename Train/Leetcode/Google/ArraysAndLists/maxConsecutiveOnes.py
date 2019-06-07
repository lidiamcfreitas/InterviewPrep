class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m, current = 0, 0

        for elem in nums:
            current = current + 1 if elem else 0
            m = max(m, current)
        return m
