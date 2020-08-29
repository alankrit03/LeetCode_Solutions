class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0

        n = len(citations)
        count = [0] * (n + 1)

        for x in citations:
            count[min(x, n)] += 1

        total = 0
        for i in range(n, -1, -1):
            total += count[i]
            if total >= i:
                return i
        return 0