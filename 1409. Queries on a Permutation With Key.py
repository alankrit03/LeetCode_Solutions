class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        cache = {x: x - 1 for x in range(1, m + 1)}
        n = len(queries)
        ans = [0] * n

        for i in range(n):
            curr = queries[i]
            ans[i] = cache[curr]
            pos = cache[curr]

            for j in cache.keys():
                if cache[j] < pos:
                    cache[j] += 1
            cache[curr] = 0
        return ans