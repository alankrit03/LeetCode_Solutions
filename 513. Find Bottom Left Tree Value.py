# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = deque()
        queue.append((root, 0))
        ans = root.val
        level = 0
        while queue:
            x = queue.popleft()
            if level != x[1]:
                ans = x[0].val
                level = x[1]

            if x[0].left:
                queue.append((x[0].left, x[1] + 1))
            if x[0].right:
                queue.append((x[0].right, x[1] + 1))
        return ans