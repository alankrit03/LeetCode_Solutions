class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        if n == k:
            return total

        s = n - k
        curr = sum(cardPoints[:s])
        ans = total - curr
        i = 0
        while s < n:
            curr += cardPoints[s] - cardPoints[i]
            ans = max(ans, total - curr)
            i += 1
            s += 1
        return ans