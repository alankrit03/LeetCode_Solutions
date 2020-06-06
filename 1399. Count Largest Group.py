from collections import Counter


class Solution:
    def countLargestGroup(self, n: int) -> int:
        cache = {1: 1}

        for i in range(2, n + 1):
            sum_ = sum(map(int, list(str(i))))

            if cache.get(sum_):
                cache[sum_] += 1
            else:
                cache[sum_] = 1
        # print(cache)
        cache = Counter(cache.values())
        return cache[max(cache.keys())]