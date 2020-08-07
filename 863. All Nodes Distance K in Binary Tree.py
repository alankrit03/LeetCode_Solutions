# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def dfs(node, parent):
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root, None)

        queue = collections.deque()
        queue.append((target, 0))

        visited = {target}

        while queue:
            d = queue[0][1]
            if d == K:
                return [node.val for node, d in queue]

            node, d = queue.popleft()

            for neighbor in (node.left, node.right, node.parent):
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, d + 1))
        return []
