class Solution:
    def threeSum(self, nums):
        def find2sum(cons, start, target):
            j = n - 1
            i = start
            while j > i:
                if (i > start and nums[i] == nums[i - 1]):
                    i += 1
                    continue
                if nums[i] + nums[j] == target:
                    print([cons, nums[i], nums[j]])
                    result.append([cons, nums[i], nums[j]])
                    i += 1
                elif nums[i] + nums[j] > target:
                    j -= 1
                else:
                    i += 1

        nums.sort()
        print(nums)
        result = []
        n = len(nums)
        for i in range(n - 2):
            if (i == 0 or (i > 0 and nums[i] != nums[i - 1])):
                find2sum(nums[i], i + 1, 0 - nums[i])
                # print()

        return result


ob = Solution()
nums=[-1,0,1,2,-1,4,5,2,3,1,0,-1,2,4,-4]
print(ob.threeSum(nums))