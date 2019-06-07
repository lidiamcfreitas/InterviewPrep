class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # cheating

        try:
            float(s)
        except Exception:
            return False
        return True

a = Solution()
print(a.isNumber('0'))