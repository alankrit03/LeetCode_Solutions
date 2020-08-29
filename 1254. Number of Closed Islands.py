class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        if not row or not col:
            return 0

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        def dfs(i, j):
            if i < 0 or j < 0 or i >= row or j >= col:
                return False
            if grid[i][j]:
                return True

            grid[i][j] = 1

            flag = True
            for d in range(4):
                flag = flag & dfs(i + dr[d], j + dc[d])

            return flag

        ans = 0
        for i in range(row):
            for j in range(col):
                if not grid[i][j]:
                    if dfs(i, j):
                        ans += 1

        # print (grid)
        return ans