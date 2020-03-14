"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return

        queue = [(0, root)]
        curr = 0

        while queue:
            temp = queue.pop(0)
            if queue:
                if queue[0][0] == temp[0]:
                    temp[1].next = queue[0][1]

            if temp[1].left:
                queue.append((temp[0] + 1, temp[1].left))
            if temp[1].right:
                queue.append((temp[0] + 1, temp[1].right))

        return root