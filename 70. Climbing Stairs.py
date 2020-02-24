class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def memo_stair(i):
            if cache.get(i):
                return cache[i]
            if i == 0:
                return 1
            elif i < 3:
                return i

            else:
                temp = memo_stair(i - 1) + memo_stair(i - 2)

            cache[i] = temp
            return temp

        return memo_stair(n)