class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if not n:
            return 0

        for i in range(n):
            if not nums[i]:
                nums[i] = -1

        cache = {0: -1}
        sum_ = 0
        ans = 0

        for i in range(n):
            sum_ += nums[i]
            if sum_ in cache:
                ans = max(ans, i - cache[sum_])
            else:
                cache[sum_] = i

        return ans