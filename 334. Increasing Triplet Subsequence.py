class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums:
            return False

        first = nums[0]
        sec = None
        for i in range(1, len(nums)):
            x = nums[i]
            try:
                if x > sec:
                    return True
            except:
                pass
            if x > first:
                sec = x
            else:
                first = x
        return False