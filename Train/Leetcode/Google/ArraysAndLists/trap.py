import math


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_i = -1
        max_v = -math.inf
        l = len(height)
        water = 0

        # find maximum
        for i in range(l):
            if height[i] > max_v:
                max_v = height[i]
                max_i = i

        for interval in (range(max_i+1), range(l - 1, max_i, -1)):
            max_seen = 0
            for j in interval:
                if max_seen < height[j]:
                    max_seen = height[j]
                else:
                    water += max_seen - height[j]

        return water


s = Solution()
test = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  # 6
print(s.trap(test))
