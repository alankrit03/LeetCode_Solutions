# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.ans = 0
        queue = deque()
        queue.append((root, 0))
        curr = 0

        while queue:
            temp = queue.popleft()
            if temp[1] == curr:
                self.ans += temp[0].val
            else:
                self.ans = temp[0].val
                curr = temp[1]

            if temp[0].left:
                queue.append((temp[0].left, temp[1] + 1))

            if temp[0].right:
                queue.append((temp[0].right, temp[1] + 1))
        return self.ans