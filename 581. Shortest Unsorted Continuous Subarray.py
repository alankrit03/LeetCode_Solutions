class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        arr = sorted(nums)

        for i in range(n):
            if nums[i] != arr[i]:
                break

        for j in range(n - 1, -1, -1):
            if nums[j] != arr[j]:
                break

        print(j, i)
        if j - i <= 0:
            return 0
        return j - i + 1
