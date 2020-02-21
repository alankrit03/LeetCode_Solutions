# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def is_equal(r1, r2):
            if not r1 and not r2:
                return True
            if not r1 or not r2:
                return False

            return (r1.val == r2.val) and is_equal(r1.right, r2.left) and is_equal(r1.left, r2.right)

        if not root:
            return True
        else:
            return is_equal(root.left, root.right)