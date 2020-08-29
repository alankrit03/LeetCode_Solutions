from functools import lru_cache


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        time = [1, 7, 30]
        n = len(days)

        @lru_cache(None)
        def recur(i):
            if i >= n:
                return 0

            ans = 10e10
            j = i
            for cost, day in zip(costs, time):
                while j < n and days[j] < days[i] + day:
                    j += 1
                ans = min(ans, recur(j) + cost)

            return ans

        return recur(0)