class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def findNextGreater(idx, x):
            ans = nums[idx]
            pos = idx
            for i in range(idx, n):
                if x < nums[i] < ans:
                    ans = nums[i]
                    pos = i
            return pos

        def customSort(idx):
            temp = nums[idx:]
            temp.sort()
            j = 0
            for i in range(idx, n):
                nums[i] = temp[j]
                j += 1

        n = len(nums)
        if n < 2:
            return None

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pos = findNextGreater(i + 1, nums[i])
                nums[pos], nums[i] = nums[i], nums[pos]
                customSort(i + 1)
                break
        else:
            nums.reverse()

        return None