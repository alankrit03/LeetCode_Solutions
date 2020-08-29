class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        graph = {}

        for x, y in paths:
            graph[x] = y

        def dfs(node):
            if node not in graph:
                return node

            return dfs(graph[node])

        return dfs(y)