from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def DFS(node, curr):
            if self.hascycle:
                return

            self.visited[node] = True
            curr.add(node)

            for neighbor in graph[node]:
                if neighbor in curr:
                    self.hascycle = 1
                    return
                if not self.visited[neighbor]:
                    DFS(neighbor, curr)

            self.ordering[self.i] = node
            self.i -= 1
            curr.remove(node)

        graph = defaultdict(set)

        for x in prerequisites:
            graph[x[1]].add(x[0])

        self.hascycle = False
        self.ordering = [0] * numCourses
        self.visited = [False] * numCourses
        self.i = numCourses - 1

        for node in range(numCourses):
            if not self.visited[node]:
                DFS(node, set())

        if self.hascycle:
            return

        return self.ordering


ob = Solution()
n = 4
preq = [[1,0],[2,0],[3,1],[3,2]]
print(ob.findOrder(n,preq))