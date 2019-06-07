class Solution(object):
    # def isOneEditDistance(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: bool
    #     """
    #
    #     if abs(len(s) - len(t)) == 1:
    #         # deletion insertion
    #         if len(t)- len(s) == -1:  # make t the largest
    #             s, t = t, s
    #         for i in range(len(t)-1):
    #             if t[i] != s[i]:
    #                 if t[i+1:] == s[i:]:
    #                     return True
    #                 else:
    #                     return False
    #         return True
    #     elif abs(len(s) - len(t)) == 0:
    #         # substitution
    #         for i in range(len(s)):
    #             if s[i] != t[i]:
    #                 if s[i+1:] == t[i+1:]:
    #                     return True
    #                 else:
    #                     return False
    #     return False

    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l_s, l_t = len(s), len(t)
        len_diff = abs(l_s - l_t)

        if (not s and not t) or s == t:
            return False

        if len_diff == 1 or len_diff == 0:
            for i in range(min(l_s, l_t)):
                if s[i] != t[i]:
                    if s[i+1:] == t[i+1:] or s[i+1:] == t[i:] or t[i+1:] == s[i:]:
                        return True
                    else:
                        return False
            return True
        return False


a = Solution()
print(a.isOneEditDistance('abcdabc', 'abcabc'))
print(a.isOneEditDistance('abcabc', 'abcdabc'))
print(a.isOneEditDistance('abcdabc', 'abcxabc'))
print(a.isOneEditDistance('abcdabc', 'ababc'))  # False
print(a.isOneEditDistance('abcdabc', 'abcsdmabc'))  # False
print(a.isOneEditDistance('', 'a'))  # True
print(a.isOneEditDistance('a', 'ac'))  # True

'''
True
True
True
False
False
True
True
'''