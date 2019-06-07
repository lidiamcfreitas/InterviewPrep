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

    def solve(self, *args):
        print(self.isPalindrome(*args))


a = Solution()

a.solve("A man, a plan, a canal: Panama")
a.solve('a raCE car')
