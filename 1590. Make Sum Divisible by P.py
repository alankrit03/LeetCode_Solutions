class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        sum_ = 0
        cache = {0: -1}
        mod = sum(nums) % p
        ans = n
        if not mod:
            return 0
        for i in range(n):
            sum_ += nums[i]
            curr = sum_ % p

            if curr >= mod:
                if curr - mod in cache:
                    ans = min(ans, i - cache[curr - mod])

            else:
                if p + curr - mod in cache:

                    ans = min(ans, i - cache[p + curr - mod])

            cache[curr] = i

        if ans == n:
            return -1
        return ans