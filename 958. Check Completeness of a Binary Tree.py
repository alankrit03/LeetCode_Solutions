# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = collections.deque()
        queue.append(root)
        emptyOccurred = False
        while queue:
            curr = queue.popleft()
            if not curr:
                emptyOccurred = True
                continue
            else:
                if emptyOccurred:
                    return False

            queue.append(curr.left)
            queue.append(curr.right)

        return True
