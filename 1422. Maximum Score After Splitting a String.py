class Solution:
    def maxScore(self, s: str) -> int:
        zero = 0
        one = s.count('1')
        ans = -math.inf
        for i in range(len(s) - 1):
            x = s[i]
            if x == '0':
                zero += 1
            elif x == '1':
                one -= 1
            ans = max(ans, zero + one)

        return ans