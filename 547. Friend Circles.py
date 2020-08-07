class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def DFS(j):
            for i in range(n):
                if M[i][j] and (i not in self.visited):
                    self.visited.add(i)
                    DFS(i)

        n = len(M)
        self.visited = set()
        self.groups = 0

        for j in range(n):
            if j not in self.visited:
                self.visited.add(j)
                self.groups += 1
                DFS(j)

        return self.groups