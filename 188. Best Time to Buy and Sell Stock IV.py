class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if not n:
            return 0
        if 2 * k > n:
            ans = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    ans += prices[i] - prices[i - 1]
            return ans


        dp = [[0] * n for i in range(k + 1)]
        for i in range(1, k + 1):
            max_ = -prices[0]
            for j in range(1, n):
                curr = -prices[j - 1] + dp[i - 1][j - 1]
                if max_ < curr:
                    max_ = dp[i - 1][j - 1] - prices[j - 1]

                dp[i][j] = max(max_ + prices[j], dp[i][j - 1])

        return dp[-1][-1]