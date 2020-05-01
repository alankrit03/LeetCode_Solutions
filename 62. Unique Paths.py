"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""


class Solution:
    def uniquePaths(self, col: int, row: int) -> int:
        dp = [[0] * col for _ in range(row)]

        for j in range(col - 1, -1, -1):
            dp[row - 1][j] = 1

        for i in range(row - 1, -1, -1):
            dp[i][col - 1] = 1

        for i in range(row - 2, -1, -1):
            for j in range(col - 2, -1, -1):
                dp[i][j] += dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]