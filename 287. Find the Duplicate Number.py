class Solution:
    def findDuplicate(self, nums) -> int:
        cache = {}
        for x in nums:
            if cache.get(x):
                return x
            else:
                cache[x] = 1


obj = Solution()
print(obj.findDuplicate([1,3,4,2,2]))