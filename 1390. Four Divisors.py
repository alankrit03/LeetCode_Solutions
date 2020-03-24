class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        cache = {}

        def div(x):
            if x % (x ** 0.5) == 0:
                return 0
            sum_ = 0
            fac = 0

            for i in range(1, int(x ** 0.5) + 1):
                if x % i == 0:
                    if fac == 2:
                        return 0
                    else:
                        fac += 1
                        sum_ += i
                        sum_ += x // i
            if fac == 2:
                return sum_
            else:
                return 0

        for num in nums:

            if cache.get(num):
                ans += cache[num]
            else:
                cache[num] = div(num)
                ans += cache[num]

        return ans