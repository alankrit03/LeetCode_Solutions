class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cache = {}

        for i in range(len(nums)):
            x = nums[i]
            if x in cache and i - cache[x] <= k:
                return True
            cache[x] = i

        return False