"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def recur(root):
            if not root:
                return 0

            height = 0
            for node in root.children:
                height = max(height, recur(node))

            return height + 1

        return recur(root)