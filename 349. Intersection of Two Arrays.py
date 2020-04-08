class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cache = {}
        for x in nums1:
            if not cache.get(x):
                cache[x] = 1

        ans = []
        for x in nums2:
            if cache.get(x) and cache[x] == 1:
                ans.append(x)
                cache[x] = 2

        return ans