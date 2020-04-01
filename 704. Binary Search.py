class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums)

        while h - l > 1:
            m = (h + l) // 2

            if target >= nums[m]:
                l = m
            else:
                h = m

        if nums[l] == target:
            return l
        return -1