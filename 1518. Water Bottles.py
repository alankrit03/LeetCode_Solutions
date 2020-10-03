class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        empty = numBottles

        while empty >= numExchange:
            newBottles = empty // numExchange
            ans += newBottles

            empty = newBottles + empty % numExchange

        return ans