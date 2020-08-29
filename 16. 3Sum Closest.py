class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        self.sum = float('inf')
        n = len(nums)
        for k in range(n - 2):
            i = k + 1
            j = n - 1
            curr = nums[k]
            while i < j:
                sum_ = curr + nums[i] + nums[j]
                rem = abs(target - sum_)
                if abs(target - self.sum) > rem:
                    self.sum = sum_

                if sum_ > target:
                    j -= 1
                elif sum_ < target:
                    i += 1
                else:
                    i += 1
                    j -= 1

        return self.sum