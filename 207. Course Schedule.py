class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def DFS(node, path):
            if self.hascycle:
                return

            self.visited[node] = True
            path.add(node)

            for neighbor in graph[node]:
                if neighbor in path:
                    self.hascycle = True
                    return
                if not self.visited[neighbor]:
                    DFS(neighbor, path)

            path.remove(node)

        graph = defaultdict(set)
        for i, j in prerequisites:
            graph[i].add(j)

        self.visited = [False] * numCourses
        self.hascycle = False

        for node in range(numCourses):
            if not self.visited[node]:
                DFS(node, set())

        if self.hascycle:
            return False
        return True