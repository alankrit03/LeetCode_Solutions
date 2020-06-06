# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.arr = []

        def recur(root):
            if not root:
                return

            recur(root.left)
            self.arr.append(root.val)
            recur(root.right)

        recur(root)

        ans = float('inf')
        for i in range(1, len(self.arr)):
            ans = min(ans, self.arr[i] - self.arr[i - 1])
        return ans