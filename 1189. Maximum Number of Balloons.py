class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = collections.Counter(text)

        ans = math.inf
        cache = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        for x in cache.keys():
            ans = min(ans, c.get(x, 0) // cache[x])
        return ans