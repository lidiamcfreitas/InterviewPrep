# Author: Lidia Freitas
# Start date: # check iPad
# Finish date: 15:49 8-4-2018


class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        S = S.upper().replace('-', '')
        res = ""
        j = 1
        for i in range(len(S)-1,-1, -1):
            if j % K != 0:
                res = S[i] + res
            else:
                if i != 0:
                    res = '-' + S[i] + res
                else:
                    res = S[i] + res
            j += 1

        return res


a = Solution()
print(a.licenseKeyFormatting(S="2-5g-3-J", K=2))        # "2-5G-3J"
print(a.licenseKeyFormatting(S="5F3Z-2e-9-w", K=4))     # "5F3Z-2E9W"
