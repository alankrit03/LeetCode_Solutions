# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys

sys.setrecursionlimit(10 ** 7)


class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0:
            return []

        def makeFBT(n):
            if n == 1:
                root = TreeNode()
                return [root]

            ans = []

            for i in range(1, n - 1, 2):
                left = makeFBT(i)
                right = makeFBT(n - i - 1)
                for x in left:
                    for y in right:
                        ans.append(TreeNode(0, left=x, right=y))

            return ans

        return makeFBT(N)
        return [TreeNode()]