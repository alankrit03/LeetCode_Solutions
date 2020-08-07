class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:

        if not grid or not grid[0]:
            return

        n = len(grid)
        m = len(grid[0])

        self.start_color = grid[r0][c0]
        self.seen = [[False] * m for i in range(n)]

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or self.seen[i][j]:
                return

            if grid[i][j] != self.start_color:
                return True
            self.seen[i][j] = True

            if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                grid[i][j] = color

            for d in range(4):

                if dfs(i + dr[d], j + dc[d]):
                    grid[i][j] = color

        dfs(r0, c0)

        return grid