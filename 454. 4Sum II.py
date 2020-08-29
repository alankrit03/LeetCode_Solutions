class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        cache1 = {}
        for x in A:
            for y in B:
                cache1[x + y] = cache1.get(x + y, 0) + 1

        cache2 = {}
        for x in C:
            for y in D:
                cache2[x + y] = cache2.get(x + y, 0) + 1

        # print(cache1)
        # print(cache2)
        ans = 0
        for key, val in cache1.items():
            ans += val * cache2.get(0 - key, 0)

        return ans