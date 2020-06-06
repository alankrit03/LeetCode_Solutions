class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = set(i for i in range(1, len(nums) + 1))

        for x in nums:
            if x in ans:
                ans.remove(x)

        return list(ans)