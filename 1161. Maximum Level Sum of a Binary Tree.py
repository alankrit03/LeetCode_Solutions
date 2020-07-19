# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = deque()
        queue.append((root, 1))
        self.maxSum = -10e9
        self.ans = 1
        currLevel = 1
        currLevelSum = 0

        while queue:
            temp = queue.popleft()

            if temp[1] == currLevel:
                currLevelSum += temp[0].val
            else:
                if currLevelSum > self.maxSum:
                    self.maxSum = currLevelSum
                    self.ans = currLevel
                currLevelSum = temp[0].val
                currLevel = temp[1]

            if temp[0].left:
                queue.append((temp[0].left, temp[1] + 1))
            if temp[0].right:
                queue.append((temp[0].right, temp[1] + 1))

        if currLevelSum > self.maxSum:
            self.maxSum = currLevelSum
            self.ans = currLevel

        return self.ans