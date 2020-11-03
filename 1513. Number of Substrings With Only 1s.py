class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        count = 0
        for x in s:
            if x == '1':
                count += 1
                ans += count
            else:
                count = 0

        return ans % 1000000007