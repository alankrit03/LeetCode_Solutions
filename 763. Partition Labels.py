class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def SortFn(x):
            return x[0]

        cache = {}
        n = len(s)
        for i in range(n):
            x = s[i]
            if x in cache:
                cache[x][1] = i
            else:
                cache[x] = [i, i]

        # print(set(s))
        cache = list(cache.values())
        cache.sort(key=SortFn)
        # print(cache)

        ans = []
        end = cache[0][1]
        start = 0
        for x in cache:
            if end >= x[0]:
                end = max(end, x[1])
            else:
                ans.append(end - start + 1)
                end = x[1]
                start = x[0]
        ans.append(end - start + 1)
        return ans