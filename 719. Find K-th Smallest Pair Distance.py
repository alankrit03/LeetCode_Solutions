class Solution:
    def smallestDistancePair(self, nums, k: int) -> int:
        nums.sort()
        n = len(nums)

        def upper(x, l):
            h = n
            while h-l > 1:
                mid = (l + h) // 2
                if nums[mid] > x:
                    h = mid
                else:
                    l = mid
            return l

        def ispossible(x):
            count = 0
            for i in range(n - 1):
                count += upper(nums[i] + x, i) - i

            if count >= k:
                return True
            return False

        l, h = 0, nums[-1] - nums[0]

        while l < h:
            mid = (l + h) // 2

            if ispossible(mid):
                h = mid
            else:
                l = mid + 1
        return l

ob = Solution()

print(ob.smallestDistancePair([3,2,5,2,1],3))