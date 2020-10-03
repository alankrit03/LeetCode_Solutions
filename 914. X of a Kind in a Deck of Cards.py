class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        c = list(collections.Counter(deck).values())

        def hcf(m, n):
            while n:
                m, n = n, m % n
            return m

        ans = c[0]
        for i in range(1, len(c)):
            ans = hcf(ans, c[i])

        return ans >= 2