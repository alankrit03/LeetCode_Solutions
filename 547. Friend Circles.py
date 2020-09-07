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


"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
APPROACH 2 : Disjoin Set Union
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        path = [i for i in range(n)]
        self.components = n

        def find(x):
            while path[x] != x:
                x = path[x]
            return x

        def union(x, y):
            x = find(x)
            y = find(y)

            if x == y:
                return

            path[x] = y
            self.components -= 1

        for i in range(n):
            for j in range(n):
                if M[i][j]:
                    union(i, j)

        return self.components