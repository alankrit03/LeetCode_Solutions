class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])

        dr = [-1,0,1,0]
        dc = [0,1,0,-1]

        def dfs(i, j):
            """This function here works recursively and changes all touching '1' to '0'.
            This ensures that one island is counted only a single time."""
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return

            grid[i][j] = '0'

            for d in range(4):
                dfs(i+dr[d], j+dc[d])

        for i in range(m):
            for j in range(n):
                """This is main working loop.
                If we get any '1' here then we pass on the co-ordinates to 'BFS' function."""
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)

        return ans
