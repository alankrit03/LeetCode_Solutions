class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_digit(x):
            ans = 0
            while x:
                ans += (x % 10) ** 2
                x //= 10
            return ans

        cache = {n: 1}

        while 1:
            n = sum_digit(n)
            if n == 1:
                return True
            if cache.get(n):
                return False

            cache[n] = 1