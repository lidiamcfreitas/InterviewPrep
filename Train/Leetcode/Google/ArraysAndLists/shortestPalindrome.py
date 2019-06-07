class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        abc = set(list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"))
        s = [char.lower() for char in s if char in abc]

        for i in range(len(s) // 2):
            if s[i] != s[-i-1]:
                return False
        return True

    def shortestPalindrome(self, s):
        if not s:
            return s

        for i in range(len(s)-1, -1, -1):
            if self.isPalindrome(s[0:i]):
                return s[i:][::-1] + s

    def solve(self, *args):
        print(self.shortestPalindrome(*args))


a = Solution()

a.solve("aacecaaa")
a.solve('abcd')
a.solve('')