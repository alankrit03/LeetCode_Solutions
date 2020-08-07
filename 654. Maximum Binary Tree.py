# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def recur(i, j):
            if i > j:
                return None
            if i == j:
                return TreeNode(nums[i])

            idx = i
            for z in range(i, j + 1):
                if nums[z] > nums[idx]:
                    idx = z

            node = TreeNode(nums[idx])
            node.left = recur(i, idx - 1)
            node.right = recur(idx + 1, j)
            return node

        node = recur(0, len(nums) - 1)
        return node