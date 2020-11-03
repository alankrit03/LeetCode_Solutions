class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        n = len(tokens)

        ans = 0
        curr = 0
        i = 0
        j = n - 1

        while i <= j:
            if P >= tokens[i]:
                P -= tokens[i]
                curr += 1
                i += 1
                ans = max(ans, curr)
            else:
                if curr:
                    P += tokens[j]
                    j -= 1
                    curr -= 1
                else:
                    break
        return ans