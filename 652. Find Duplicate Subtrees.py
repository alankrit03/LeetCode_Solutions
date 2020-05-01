# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        cache = set()
        ans = []
        ans_cache = set()
        if not root:
            return

        def recur(root):
            if not root:
                return 'null'
            x = recur(root.left)
            y = recur(root.right)
            if (root.val, (x, y)) in cache and (root.val, (x, y)) not in ans_cache:
                ans.append(root)
                ans_cache.add((root.val, (x, y)))
            else:
                cache.add((root.val, (x, y)))

            return (root.val, (x, y))

        recur(root)
        return ans