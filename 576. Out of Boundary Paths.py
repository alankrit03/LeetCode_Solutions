class Solution:
    def findPaths(self, row: int, col: int, N: int, i: int, j: int) -> int:
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        def dfs(i, j, k, cache={}):
            if i < 0 or j < 0 or i >= row or j >= col:
                return 1
            if not k:
                return 0

            if (i, j, k) in cache:
                return cache[(i, j, k)]

            ans = 0

            for d in range(4):
                ans += dfs(i + dr[d], j + dc[d], k - 1, cache)

            cache[(i, j, k)] = ans

            return ans

        return dfs(i, j, N) % 1000000007