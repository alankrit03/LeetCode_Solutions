class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        if not nums:
            return False

        cache = {0: -1}
        rem = 0

        for i in range(len(nums)):
            try:
                rem = (rem + nums[i]) % k
            except ZeroDivisionError:
                rem = rem + nums[i]

            if rem in cache:
                if i - cache[rem] > 1:
                    return True
            else:
                cache[rem] = i

        return False

ob = Solution()
print(ob.checkSubarraySum([23,4,5,6],0))