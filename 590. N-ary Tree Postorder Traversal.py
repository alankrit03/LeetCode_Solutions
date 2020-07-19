"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.ans = []

        def recur(root):
            if not root:
                return

            for node in root.children:
                recur(node)
            self.ans.append(root.val)

        recur(root)
        return self.ans