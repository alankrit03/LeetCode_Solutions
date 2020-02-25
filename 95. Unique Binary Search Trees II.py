# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n:
            return []
        return self.helper(1, n)

    def helper(self, left, right):
        if left > right:  # No valid subtree
            return [None]

        if left == right:  # Only one choice
            return [TreeNode(left)]

        left_lst, right_lst, res = None, None, []

        for i in range(left, right + 1):

            left_lst = self.helper(left, i - 1)
            right_lst = self.helper(i + 1, right)

            for left_child in left_lst:
                for right_child in right_lst:
                    root = TreeNode(i)
                    root.left = left_child
                    root.right = right_child
                    res.append(root)
        return res