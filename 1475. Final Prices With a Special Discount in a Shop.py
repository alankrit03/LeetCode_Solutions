class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        nse = [0] * n
        stack = []
        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                nse[stack.pop()] = prices[i]
            stack.append(i)

        for i in range(n):
            prices[i] -= nse[i]
        return prices