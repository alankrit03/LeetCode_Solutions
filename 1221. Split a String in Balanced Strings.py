class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        state = 0
        for x in s:
            if x == 'R':
                state += 1
            else:
                state -= 1

            if not state:
                ans += 1
        return ans