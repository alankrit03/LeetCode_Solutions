# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        if not root:
            return

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        elif key == root.val:

            if not root.left and not root.right:
                root = None

            elif root.right:
                successor_node = self.successor(root)
                root.val = successor_node.val
                root.right = self.deleteNode(root.right, successor_node.val)

            elif root.left:
                predecessor_node = self.predecessor(root)
                root.val = predecessor_node.val
                root.left = self.deleteNode(root.left, predecessor_node.val)

        return root

    def successor(self, root):
        if not root:
            return

        if root.right:
            root = root.right

            while root.left:
                root = root.left
            return root

    def predecessor(self, root):
        if not root:
            return

        if root.left:
            root = root.left

            while root.right:
                root = root.right
            return root