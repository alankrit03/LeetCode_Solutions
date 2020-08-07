class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or (not matrix[0]):
            return 0

        self.cache = {}

        def dfs(i, j, prev=float('-infinity')):
            if i < 0 or j < 0 or i >= n or j >= m or matrix[i][j] <= prev:
                return 0
            if (i, j) in self.cache:
                return self.cache[(i, j)]
            t = 0
            for d in range(4):
                t = max(t, dfs(i + dr[d], j + dc[d], matrix[i][j]))

            self.cache[(i, j)] = t + 1
            return t + 1

        ans = 0

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(i, j))

        return ans