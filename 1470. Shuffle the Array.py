class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if not n:
            return
        ans = [0] * 2 * n

        i = idx = 0
        while i < n:
            ans[idx] = nums[i]
            idx += 1
            ans[idx] = nums[i + n]
            idx += 1
            i += 1
        return ans