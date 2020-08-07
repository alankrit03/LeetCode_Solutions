class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.paths = []
        n = len(graph)

        def recur(node, currPath):
            if node == (n - 1):
                self.paths.append(currPath[:])
                return
            edges = graph[node]

            for edge in edges:
                currPath.append(edge)
                recur(edge, currPath)
                currPath.pop()

        recur(0, [0])

        return self.paths