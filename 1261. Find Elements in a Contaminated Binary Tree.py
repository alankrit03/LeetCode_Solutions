# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root

        self.cache = set()

        def recur(node, x):
            if not node:
                return
            node.val = x
            self.cache.add(x)
            if node.left:
                recur(node.left, 2 * x + 1)
            if node.right:
                recur(node.right, 2 * x + 2)

        recur(root, 0)

    def find(self, target: int) -> bool:
        return target in self.cache

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)