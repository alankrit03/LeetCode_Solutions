class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        coins.sort()
        if coins[0] > amount:
            return -1

        dp = [0] * (amount + 1)

        for i in range(coins[0], amount + 1, coins[0]):
            dp[i] = i // coins[0]

        for idx in range(1, len(coins)):
            coin = coins[idx]
            if coin > amount:
                break
            dp[coin] = 1
            for i in range(coin + 1, amount + 1):
                if dp[i - coin]:
                    if dp[i]:
                        dp[i] = min(dp[i], dp[i - coin] + 1)
                    else:
                        dp[i] = dp[i - coin] + 1

        print(coins)
        if dp[-1] == 0:
            return -1
        return dp[-1]
