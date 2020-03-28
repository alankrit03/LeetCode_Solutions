# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.n = 0
        self.stack = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.stack.insert(0, root.val)
            self.n += 1
            inorder(root.right)

        inorder(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.n -= 1
        return self.stack.pop()

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.n > 0:
            return True

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()