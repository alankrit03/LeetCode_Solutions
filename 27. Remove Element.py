class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        i, j = 0, len(nums) - 1

        while j - i > 0:

            if nums[j] == val:
                while j > i and nums[j] == val:
                    j -= 1

            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]

            else:
                i += 1
        if nums[j] == val:
            return j
        return j + 1