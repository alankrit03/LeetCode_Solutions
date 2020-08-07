# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        queue = collections.deque()
        if not root:
            return

        queue.append((root, 0))
        level = 0
        currSum = 0
        n = 0

        while queue:
            node, l = queue.popleft()

            if l == level:
                currSum += node.val
                n += 1
            else:
                ans.append(currSum / n)
                currSum = node.val
                n = 1
                level = l

            if node.left:
                queue.append((node.left, l + 1))
            if node.right:
                queue.append((node.right, l + 1))
        ans.append(currSum / n)
        return ans