# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val == val:
            return root

        if root.val > val:
            ans = self.searchBST(root.left, val)
        else:
            ans = self.searchBST(root.right, val)

        return ans