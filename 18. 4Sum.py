class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def find2sum(nums, target):
            res = []
            n = len(nums)
            lo, hi = 0, n - 1

            while lo < hi:
                sum_ = nums[lo] + nums[hi]

                if sum_ < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif sum_ > target or (hi < n - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
            return res

        def ksum(nums, target, k):
            n = len(nums)
            ans = []

            if not n or nums[0] * k > target or nums[-1] * k < target:
                return []

            if k == 2:
                return find2sum(nums, target)

            for i in range(n):
                if not i or nums[i - 1] != nums[i]:
                    for x in ksum(nums[i + 1:], target - nums[i], k - 1):
                        ans.append([nums[i]] + x)
            return ans

        nums.sort()
        return ksum(nums, target, 4)