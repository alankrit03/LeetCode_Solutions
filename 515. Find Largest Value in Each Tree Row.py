# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return

        queue = deque()
        queue.append((root, 0))
        curr = root.val
        level = 0
        while queue:
            x = queue.popleft()
            if level == x[1]:
                curr = max(curr, x[0].val)
            else:
                ans.append(curr)
                curr = x[0].val
                level = x[1]

            if x[0].left:
                queue.append((x[0].left, x[1] + 1))
            if x[0].right:
                queue.append((x[0].right, x[1] + 1))
        ans.append(curr)
        return ans