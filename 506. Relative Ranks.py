class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        if not nums:
            return
        ranks = list(enumerate(nums))
        ranks.sort(key=lambda x: x[1], reverse=True)
        ans = ['0'] * len(nums)
        medal = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        for i in range(len(nums)):
            if i < 3:
                ans[ranks[i][0]] = medal[i]
            else:
                ans[ranks[i][0]] = str(i + 1)

        return ans