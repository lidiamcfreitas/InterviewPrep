# Author: Lidia Freitas
# Start date: 14:54 8-4-2018
# Finish date: 15:39 8-4-2018

# Definition for a binary tree node.

import sys

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestUnivaluePath_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if (root.left is None and root.right is None):
            return 0, 0, 0, 0  # left, right, connecting, max
        else:
            left_eval = (0, 0, 0, 0) if root.left is None else self.longestUnivaluePath_recursive(root.left)
            right_eval = (0, 0, 0, 0) if root.right is None else self.longestUnivaluePath_recursive(root.right)

            left_v = 0 if root.left is None or (root.left.val != root.val) else max(left_eval[0], left_eval[1]) + 1
            right_v = 0 if root.right is None or (root.right.val != root.val) else max(right_eval[0], right_eval[1]) + 1

            connecting_v = left_v + right_v
            max_v = max(left_v, right_v, connecting_v, left_eval[3], right_eval[3])
            res = left_v, right_v, connecting_v, max_v
            sys.stdout.flush()
            return res

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            return self.longestUnivaluePath_recursive(root)[3]
        else:
            return 0


'''
              5
             / \
            4   5
           / \   \
          1   1   5
          
 output: 2
'''

v_1_1 = TreeNode(1)
v_1_2 = TreeNode(1)
v_5_1 = TreeNode(5)

v_4_1 = TreeNode(4)
v_4_1.left = v_1_1
v_4_1.right = v_1_2

v_5_2 = TreeNode(5)
v_5_2.left = v_5_1

v_5_3 = TreeNode(5)
v_5_3.left = v_4_1
v_5_3.right = v_5_2
root = v_5_3

a = Solution()
#print(a.longestUnivaluePath(root))


'''
              1
             / \
            4   5
           / \   \
          4   4   5
output: 2
'''

v1 = TreeNode(4)
v2 = TreeNode(4)
v3 = TreeNode(5)

v4 = TreeNode(4)
v4.left = v1
v4.right = v2

v5 = TreeNode(5)
v5.left = v3

v6 = TreeNode(1)
v6.left = v4
v6.right = v5
root = v6

a = Solution()
#print(a.longestUnivaluePath(root))


'''
              4
             / \
            4   4
           / \   \
          4   4   4
output: 4
'''

v1 = TreeNode(4)
v2 = TreeNode(4)
v3 = TreeNode(4)

v4 = TreeNode(4)
v4.left = v1
v4.right = v2

v5 = TreeNode(4)
v5.left = v3

v6 = TreeNode(4)
v6.left = v4
v6.right = v5
root = v6

a = Solution()
#print(a.longestUnivaluePath(root))

'''
              4
             / \
            4   4
           / \   \
          1   4   4
output: 4
'''

v1 = TreeNode(1)
v2 = TreeNode(4)
v3 = TreeNode(4)

v4 = TreeNode(4)
v4.left = v1
v4.right = v2

v5 = TreeNode(4)
v5.left = v3

v6 = TreeNode(4)
v6.left = v4
v6.right = v5
root = v6

a = Solution()
#print(a.longestUnivaluePath(root))

v1 = TreeNode(1)
v2 = TreeNode(1)
v2.right = v1

print(a.longestUnivaluePath(v2))

