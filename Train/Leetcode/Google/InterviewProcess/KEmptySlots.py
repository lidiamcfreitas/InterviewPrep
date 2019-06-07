# Author: Lidia Freitas
# Start date: 13:46 8-4-2018
# Finish date: 14:21 8-4-2018


class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        size = len(flowers)
        blooming = set()

        def false_interval(i, j):
            min_v = min(i,j)
            max_v = max(i,j)
            for k in range(min_v+1, max_v):
                if k in blooming:
                    return False
            return True

        for day, i in enumerate(flowers):
            i -= 1
            for j in (i - k - 1, i + k + 1):
                # print(i,j, blooming)
                # print("j in set", j in blooming)
                if 0 <= j < size and j in blooming:
                    # print(false_interval(i,j), "false interval")
                    if false_interval(i, j):
                        return day + 1

            blooming.add(i)
        return -1


# test
a = Solution()
print(a.kEmptySlots(flowers=[1, 3, 2], k=1))  # 2
print(a.kEmptySlots(flowers=[1, 2, 3], k=1))  # -1
print(a.kEmptySlots(flowers=[1, 2, 3, 7, 4, 5, 6], k=1))  # 6
print(a.kEmptySlots(flowers=[1, 2, 3, 7, 4, 5, 6], k=3))  # 4
print(a.kEmptySlots(flowers=[1, 2, 3, 7, 4, 5, 6], k=2))  # 5
print(a.kEmptySlots(flowers=[1, 2, 3, 7, 4, 5, 6], k=9))  # -1
