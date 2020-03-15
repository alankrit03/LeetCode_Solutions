# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __storenode(self, root, nodes):
        if not root:
            return

        self.__storenode(root.left, nodes)
        nodes.append(root)
        self.__storenode(root.right, nodes)

    def __buildTree(self, nodes, start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        node = nodes[mid]

        node.left = self.__buildTree(nodes, start, mid - 1)
        node.right = self.__buildTree(nodes, mid + 1, end)
        return node

    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        self.__storenode(root, nodes)

        n = len(nodes)
        return self.__buildTree(nodes, 0, n - 1) 