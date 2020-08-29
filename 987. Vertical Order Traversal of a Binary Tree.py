# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        def sortFn(x):
            return (x[1], x[0])

        if not root:
            return
        self.cache = {}
        leftmost = +1
        rightmost = -1

        queue = collections.deque()
        queue.append((root, 0, 0))
        while queue:
            node, level, width = queue.popleft()

            leftmost = min(width, leftmost)
            rightmost = max(width, rightmost)

            try:
                self.cache[width].append((node.val, level))
            except:
                self.cache[width] = [(node.val, level)]

            if node.left:
                queue.append((node.left, level + 1, width - 1))
            if node.right:
                queue.append((node.right, level + 1, width + 1))

        ans = []
        for i in range(leftmost, rightmost + 1):
            self.cache[i].sort(key=sortFn)
            ans.append([x for x, y in self.cache[i]])
        return ans