from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = Counter(nums)
        ans = 0
        for x in c:
            d = c[x]
            ans += (d*(d-1))//2
        return ans