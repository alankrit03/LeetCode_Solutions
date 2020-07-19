"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return
        self.ans = []

        queue = deque()
        queue.append((root, 0))
        curr = 0
        tempArr = []
        while queue:
            temp = queue.popleft()

            if curr == temp[1]:
                tempArr.append(temp[0].val)
            else:
                self.ans.append(tempArr)
                tempArr = [temp[0].val]
                curr = temp[1]

            for node in temp[0].children:
                queue.append((node, temp[1] + 1))
        self.ans.append(tempArr)
        return self.ans