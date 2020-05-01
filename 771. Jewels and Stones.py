class Solution:
    from collections import Counter
    def numJewelsInStones(self, J: str, S: str) -> int:
        c = Counter(S)

        ans = 0
        for x in J:
            if x in c:
                ans += c[x]
        return ans