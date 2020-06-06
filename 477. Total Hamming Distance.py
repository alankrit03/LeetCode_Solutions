class Solution:
    def totalHammingDistance(self, nums: List[int]):
        if not nums:
            return 0
        n = max(nums)

        ans = zero = one = 0
        mask = 1

        while mask <= n:
            zero = one = 0
            for num in nums:
                if mask ^ num == num - mask:
                    one += 1
                else:
                    zero += 1

            ans += zero * one
            mask *= 2

        return ans