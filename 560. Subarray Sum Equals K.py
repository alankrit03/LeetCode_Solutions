class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cache = {0: 1}

        sum_ = 0
        ans = 0

        for i in range(len(nums)):
            sum_ += nums[i]
            if cache.get(sum_ - k):
                ans += cache[sum_ - k]
            if cache.get(sum_):
                cache[sum_] += 1
            else:
                cache[sum_] = 1

        return ans