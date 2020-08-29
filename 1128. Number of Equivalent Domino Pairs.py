class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cache = {}

        for x, y in dominoes:
            if (x, y) in cache:
                cache[(x, y)] += 1
            elif (y, x) in cache:
                cache[(y, x)] += 1
            else:
                cache[(x, y)] = 1
        print(cache)

        ans = 0
        for x, y in cache.items():
            ans += (y * (y - 1)) // 2

        return ans