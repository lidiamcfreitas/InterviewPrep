class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = 0
        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            if i != 0:
                if digits[i] < 9:
                    return digits
                elif digits[i] == 10:
                    digits[i-1] += 1
                    digits[i] = 0
            else:
                if digits[i] < 9:
                    return digits
                else:
                    digits = [1] + digits
                    return digits

a = Solution()
x = [9,9,9]
print(a.plusOne(x))
