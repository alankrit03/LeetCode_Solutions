class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k = 3
        if not prices:
            return 0
        n = len(prices)

        dp = [[0] * n for i in range(k)]

        for i in range(1, k):
            max_ = -prices[0]
            t = 0
            for j in range(1, n):
                curr = dp[i - 1][j - 1] - prices[j - 1]
                if curr > max_:
                    max_ = curr
                    t = j - 1
                dp[i][j] = max(max_ + prices[j], dp[i][j - 1])
        return dp[-1][-1]