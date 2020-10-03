class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        cache = {1: 0}

        def power(x):
            if x == 1:
                return 0

            if x in cache:
                return cache[x]

            if x % 2:
                ans = power(3 * x + 1)
            else:
                ans = power(x // 2)

            ans += 1
            cache[x] = ans
            return ans

        for i in range(lo, hi + 1):
            power(i)

        arr = [i for i in range(lo, hi + 1)]
        arr.sort(key=lambda x: cache[x])

        return arr[k - 1]