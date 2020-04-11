class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        j = 0
        n = len(nums)
        sum_ = 0

        while j < n and sum_ < s:
            sum_ += nums[j]
            j += 1

        if j == n and sum_ < s:
            return 0

        i = 0

        while j < n:

            if sum_ - nums[i] >= s:
                sum_ -= nums[i]
                i += 1
            else:
                sum_ -= nums[i]
                sum_ += nums[j]
                i += 1
                j += 1

        while sum_ >= s and i < n:
            if sum_ - nums[i] >= s:
                sum_ -= nums[i]
                i += 1
            else:
                break

        return j - i






sum_=8
arr=[2,3,1,2,4,3,1,6,2,7]

ans = Solution.minSubArrayLen(sum_,arr)
print('ans = ',ans)