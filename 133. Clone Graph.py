"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""


class Solution:
    def __init__(self):
        self.cache_clone = {}
        self.cache_set = set()

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return

        """This function clones every node in graph and stores it in the cache_clone.
        The dictionary will help to generate the relationship further in the code."""
        def clone_nodes(node):
            if not node or node in self.cache_set:
                return

            self.cache_set.add(node)
            self.cache_clone[node] = Node(node.val)

            for x in node.neighbors:
                clone_nodes(x)

        clone_nodes(node)

        """Now the members are added in neighbours list of the clones nodes.
        This is done by taking cloned nodes from the cache_clone dictionary."""
        for x in self.cache_set:
            for y in x.neighbors:
                self.cache_clone[x].neighbors.append(self.cache_clone[y])

        # for x,y in self.cache_clone.items():
        #     print(x.val , y.val)

        return self.cache_clone[node]