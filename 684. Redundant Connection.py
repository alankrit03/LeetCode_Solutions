from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(node, target):
            if node not in self.seen:
                self.seen.add(node)
                if node == target:
                    return True

                neighbors = graph[node]

                for nex in neighbors:
                    if dfs(nex, target):
                        return True

        graph = defaultdict(set)

        for x, y in edges:
            self.seen = set()
            print('graph = ', graph)
            if x in graph and y in graph and dfs(x, y):
                ans = [x, y]
            else:
                graph[x].add(y)
                graph[y].add(x)
        return ans