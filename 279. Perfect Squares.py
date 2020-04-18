import sys

sys.setrecursionlimit(10 ** 7)


class Solution:
    def numSquares(self, n: int) -> int:
        square = [1]
        i = 2
        while i ** 2 <= n:
            square.append(i ** 2)
            i += 1

        dp = [n + 1] * (n + 1)
        dp[0] = 0
        for s in square:
            for i in range(1, n + 1):
                if i >= s:
                    dp[i] = min(dp[i - s] + 1, dp[i])

        return dp[-1]