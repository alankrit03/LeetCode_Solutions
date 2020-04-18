class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache = set()

        for x in nums:
            if x in cache:
                return True
            cache.add(x)
        return False