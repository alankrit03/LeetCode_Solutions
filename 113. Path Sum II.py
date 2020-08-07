# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        self.ans = []

        def recur(node, path, total):
            if not node:
                return

            total -= node.val
            path.append(node.val)

            if (not node.left) and (not node.right):
                if not total:
                    self.ans.append(path[:])
                path.pop()
                return

            if node.left:
                recur(node.left, path, total)
            if node.right:
                recur(node.right, path, total)
            path.pop()

        recur(root, [], target)

        return self.ans