# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.arr = []

        def recur(node):
            if not node:
                return
            recur(node.left)
            self.arr.append(node.val)
            recur(node.right)

        recur(root)
        ans = 2 ** 31 - 1
        for i in range(len(self.arr) - 1, 0, -1):
            ans = min(ans, self.arr[i] - self.arr[i - 1])

        return ans