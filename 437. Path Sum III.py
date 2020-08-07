# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        self.ans = 0

        def recur(node, cache):
            if not node:
                return

            if node.val in cache:
                self.ans += cache[node.val]

            if node.val == target:
                self.ans += 1

            cache1 = defaultdict(int)
            for key, value in cache.items():
                cache1[key - node.val] += value

            cache1[target - node.val] += 1

            if node.left:
                recur(node.left, cache1)
            if node.right:
                recur(node.right, cache1)

            if cache1[target - node.val] == 1:
                cache1.pop(target - node.val)
            else:
                cache1[target - node.val] -= 1

        recur(root, defaultdict(int))

        return self.ans