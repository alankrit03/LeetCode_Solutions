class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        ans = 0
        counter = 0

        for x in S:
            if x == '(':
                counter += 1
            else:
                if not counter:
                    ans += 1
                else:
                    counter -= 1
        return ans + counter