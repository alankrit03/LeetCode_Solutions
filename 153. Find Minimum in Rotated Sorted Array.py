class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = -1, len(nums) - 1
        n = h
        while h - l > 1:
            m = (l + h) // 2

            if nums[m] > nums[n]:
                l = m
            else:
                h = m
        return nums[h]