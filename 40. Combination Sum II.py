import sys

sys.setrecursionlimit(10 ** 7)


class Solution:
    def __init__(self):
        self.ans = []

    def combinationSum2(self, candidates, target: int):
        self.cache = set()

        n = len(candidates)
        candidates.sort()

        def recur(i, sum_, temp):
            if sum_ < 1:

                if not sum_ and temp not in self.cache:
                    # print(temp)
                    self.ans.append(list(temp))
                    self.cache.add(temp)
                return
            for j in range(i, n):
                sum_ -= candidates[j]
                recur(j + 1, sum_, temp + (candidates[j],))
                sum_ += candidates[j]

        recur(0, target, tuple())

        return self.ans
