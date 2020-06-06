class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        def smaller_than(x):
            l, h = -1, n - 1

            while h - l > 1:
                m = (l + h) // 2
                if sorted_num[m] >= x:
                    h = m
                else:
                    l = m
            return h - 0

        n = len(nums)
        result = [0] * n
        sorted_num = sorted(nums)
        for i in range(n):
            result[i] = smaller_than(nums[i])
        return result