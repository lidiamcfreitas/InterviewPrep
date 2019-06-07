class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_set = ['(', '[', '{']
        close_set = [')', ']', '}']

        stack = []

        if not s:
            return True

        for char in s:
            if char in open_set:
                stack.append(char)
            else:
                if not stack:
                    return False

                open_char = open_set[close_set.index(char)]
                if open_char != stack.pop():
                    return False

        if stack:
            return False
        return True
