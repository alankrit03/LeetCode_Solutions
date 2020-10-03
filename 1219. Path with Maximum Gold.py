class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ans = 0
        row = len(grid)
        if not row:
            return 0
        col = len(grid[0])
        if not col:
            return 0

        dc = [0, 1, 0, -1]
        dr = [-1, 0, 1, 0]

        def dfs(i, j):
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] < 1:
                return 0
            t = 0
            grid[i][j] = -grid[i][j]
            for d in range(4):
                t = max(t, dfs(i + dr[d], j + dc[d]))
            grid[i][j] = -grid[i][j]
            return t + grid[i][j]

        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    gold = dfs(i, j)
                    ans = max(gold, ans)

        return ans