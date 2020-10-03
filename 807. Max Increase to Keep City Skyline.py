class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        row_max = [-1] * row
        col_max = [-1] * col

        for x in range(row):
            for y in range(col):
                row_max[x] = max(row_max[x], grid[x][y])
                col_max[x] = max(col_max[x], grid[y][x])
        print(row_max)
        print(col_max)
        ans = 0
        for i in range(row):
            for j in range(col):
                ans += min(row_max[i], col_max[j]) - grid[i][j]

        return ans