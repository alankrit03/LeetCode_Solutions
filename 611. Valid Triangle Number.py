class Solution:
    def triangleNumber(self, nums) -> int:
        def findK(x, lo):
            hi = n

            while hi - lo > 1:
                mid = (lo + hi) // 2

                if x <= nums[mid]:
                    hi = mid
                else:
                    lo = mid
            return lo

        nums.sort()
        ans = 0
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                pos = findK(nums[i] + nums[j], j)
                ans += pos - j

        return ans

ob = Solution()
arr = [2,2,2,2,2]
print(ob.triangleNumber(arr))