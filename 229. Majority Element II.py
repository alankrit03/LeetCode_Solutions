class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        c = collections.Counter(nums)
        ans = []
        for x, y in c.most_common(2):
            if y > (n // 3):
                ans.append(x)

        return ans