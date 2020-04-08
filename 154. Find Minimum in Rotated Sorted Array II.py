class Solution:
    def findMin(self, nums) -> int:
        l, h = -1, len(nums)-1
        n = h
        while h-l > 1:
            m = (l+h)//2
            if nums[max(l,0)]==nums[n]:
                l+=1
            elif nums[m] > nums[n]:
                l = m
            else:
                h = m
        return min(nums[h],nums[max(l,0)])

ob = Solution()
print(ob.findMin([3,3,3,1,3,3]))