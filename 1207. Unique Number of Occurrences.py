class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cache = {}
        for x in arr:
            try:
                cache[x] += 1
            except:
                cache[x] = 1

        cache = cache.values()
        temp = set()
        for x in cache:
            if x in temp:
                return False
            temp.add(x)

        return True