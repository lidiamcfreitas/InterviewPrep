class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        if not s:
            return 0

        i, j = 0, 0
        max_seen = 1 if k > 0 else 0
        len_s = len(s)
        dict_chars = {s[0]: 1}

        while True:
            if len(dict_chars.keys()) <= k:
                # update max
                max_seen = max(max_seen, j - i + 1)
                j += 1
                if j == len_s:
                    return max_seen
                if s[j] in dict_chars:
                    dict_chars[s[j]] += 1
                else:
                    dict_chars[s[j]] = 1
            else:
                if dict_chars[s[i]] == 1:
                    del dict_chars[s[i]]
                else:
                    dict_chars[s[i]] -= 1
                i += 1

        return max_seen


a = Solution()
print(a.lengthOfLongestSubstringKDistinct('cabcababc', 2))
print(a.lengthOfLongestSubstringKDistinct('', 2))
print(a.lengthOfLongestSubstringKDistinct("ababffzzeee", 2))
print(a.lengthOfLongestSubstringKDistinct("aa", 2))
