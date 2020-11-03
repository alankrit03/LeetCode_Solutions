class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colored = [-1] * n
        visited = [False] * n

        def dfs(node, color):
            if visited[node]:
                if colored[node] != color:
                    return False
                return True

            visited[node] = True
            colored[node] = color

            for nex in graph[node]:
                if not dfs(nex, (color + 1) % 2):
                    return False
            return True

        for node in range(n):
            if not visited[node]:
                if not dfs(node, 0):
                    return False

        return True