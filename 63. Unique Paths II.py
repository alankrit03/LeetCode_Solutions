"""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1]:
            return 0

        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0] * col for _ in range(row)]

        dp[-1][-1] = 1

        for j in range(col - 2, -1, -1):
            if obstacleGrid[row - 1][j]:
                continue
            dp[row - 1][j] += dp[row - 1][j + 1]

        for i in range(row - 2, -1, -1):
            if obstacleGrid[i][col - 1]:
                continue
            dp[i][col - 1] += dp[i + 1][col - 1]

        """This is the main loop which iteratively sums up the total number of unique paths."""
        for i in range(row - 2, -1, -1):
            for j in range(col - 2, -1, -1):
                if obstacleGrid[i][j]:
                    continue
                dp[i][j] += dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]