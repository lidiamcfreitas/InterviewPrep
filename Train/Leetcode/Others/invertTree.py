import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def print_tree(root):
    if root is None:
        return

    print('root.val', root.val)

    if root.left is not None:
        print('root.val', root.val, 'left:', root.left.val)
        print_tree(root.left)
    if root.right is not None:
        print('root.val', root.val, 'right:', root.right.val)
        print_tree(root.right)


class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return

        aux = root.left
        root.left = root.right
        root.right = aux

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


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
# print(a.invertTree(root))


'''
              1
             / \
            4   5
           / \   \
          2   1   6
output: 2
'''

v1 = TreeNode(2)
v2 = TreeNode(1)
v3 = TreeNode(6)

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
inverted = a.invertTree(root)
print(print_tree(inverted))


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
inverted = a.invertTree(root)
# print(print_tree(inverted))

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
# print(a.invertTree(root))

v1 = TreeNode(1)
v2 = TreeNode(1)
v2.right = v1




inverted = a.invertTree(v2)
# print(print_tree(inverted))


