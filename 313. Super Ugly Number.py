class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)
        start = [0] * k

        nums = [1]
        n -= 1
        while n:
            min_ = primes[0] * nums[start[0]]

            for i in range(1, k):
                min_ = min(min_, primes[i] * nums[start[i]])

            for i in range(k):
                if not min_ % primes[i]:
                    start[i] += 1

            nums.append(min_)
            n -= 1
        return nums[-1]