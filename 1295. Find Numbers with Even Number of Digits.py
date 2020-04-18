class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            if len(str(x))%2==0:
                ans +=1
        return ans