class Solution:
    def maxPower(self, s: str) -> int:
        ans = 0
        if not s:
            return 0
        curr = s[0]
        count = 0
        for x in s:
            if x==curr:
                count+=1
            else:
                ans = max(ans,count)
                count = 1
                curr = x
        ans = max(ans,count)
        return ans