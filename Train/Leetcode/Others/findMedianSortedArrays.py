class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        mn = m + n

        if not nums1:
            return self.median_array(nums2)
        if not nums2:
            return self.median_array(nums1)

        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1

        def predicate(i, j, A, B):
            return A[i-1] <= B[j] and B[j-1] <= A[i]

        lo, hi = 0, m

        while lo < hi:
            i = int(lo + (hi - lo) // 2)
            j = int((m + n) / 2 - i)

            if predicate(i, j, nums1, nums2):
                break
            elif nums2[j-1] > nums1[i]:
                lo = i + 1
            else:
                hi = i

        A, B = nums1, nums2
        if mn % 2 == 1:
            return max((A[i-1], B[j-1]))
        else:
            return (max((A[i-1], B[j-1])) + min((A[i], B[j]))) / 2

    @staticmethod
    def median_array(A):
        l_a = len(A)
        if len(A) % 2 == 1:
            return A[l_a // 2]
        else:
            return (A[l_a // 2 -1 ] + A[l_a // 2]) / 2


n1 = [1,3,5]
n2 = [1,6,7]
n3 = [1,1,3,4,6,7]

a = Solution()
print(a.findMedianSortedArrays([1], []))
