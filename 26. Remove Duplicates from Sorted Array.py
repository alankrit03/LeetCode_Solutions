class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return n

        i = j = 1
        curr = nums[0]

        while j < n:
            if nums[j] > curr:
                nums[i] = nums[j]
                curr = nums[j]
                i += 1
            j += 1
        return i