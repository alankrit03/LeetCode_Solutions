class Solution:
    def countOrders(self, n: int) -> int:
        cache = {}

        def fac(x):
            if cache.get(x):
                return cache[x]

            if x < 2:
                return 1
            else:
                temp = x * fac(x - 1)

            cache[x] = temp
            return temp

        a = fac(2 * n)
        return (a // 2 ** n) % 1000000007