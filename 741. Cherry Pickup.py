class Solution:
    def cherryPickup(self, grid) -> int:
        row = len(grid)
        if not row:
            return 0
        col = len(grid[0])
        if not col:
            return 0

        def getMax():
            dp = []
            for x in grid:
                dp.append(x[:])
            for j in range(col - 2, -1, -1):
                if grid[row - 1][j] == -1:
                    dp[row - 1][j] = 0
                else:
                    dp[row - 1][j] += dp[row - 1][j + 1]

                if grid[j][col - 1] == -1:
                    dp[j][col - 1] = 0
                else:
                    dp[j][col - 1] += dp[j + 1][col - 1]

            for i in range(row - 2, -1, -1):
                for j in range(col - 2, -1, -1):
                    if grid[i][j] == -1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] += max(dp[i + 1][j], dp[i][j + 1])

            return dp[0][0]

        self.ans = 0

        dr = [0, 1]
        dc = [1, 0]

        def dfs(i, j, cherry):
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == -1:
                return

            if (i == row - 1) and (j == col - 1):
                temp = getMax()
                self.ans = max(self.ans, cherry + temp)
                return

            temp = cherry + grid[i][j]
            grid[i][j] = 0
            for d in range(2):
                dfs(i + dr[d], j + dc[d], temp)
            grid[i][j] = temp - cherry
            return

        dfs(0, 0, 0)
        return self.ans



ob = Solution()
grid = [[0, 1, -1],
        [1, 0, -1],
        [1, 1,  1]]

print(ob.cherryPickup(grid))