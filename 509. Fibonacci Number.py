class Solution:
    def fib(self, N: int) -> int:
        cache = {}

        def memo_fib(n):
            if cache.get(n):
                return cache.get(n)
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                temp = memo_fib(n - 1) + memo_fib(n - 2)

            cache[n] = temp
            return temp

        return memo_fib(N)