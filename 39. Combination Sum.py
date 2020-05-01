"""'''''''''''''''''''''''''''''''''''''''''''
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
''''''''''''''''''''''''''''''''''''''''''''"""

import sys

sys.setrecursionlimit(10 ** 7)


class Solution:
    def __init__(self):
        self.temp = []
        self.ans = []

    def combinationSum(self, candidates, target: int):
        n = len(candidates)

        def recur(i, sum_):
            if sum_ < 1:
                if not sum_:
                    self.ans.append(self.temp[:])
                return

            for j in range(i, n):
                self.temp.append(candidates[j])
                sum_ -= candidates[j]
                recur(j, sum_)
                self.temp.pop()
                sum_ += candidates[j]

        recur(0, target)

        return self.ans

ob = Solution()
print(ob.combinationSum([2,3,6,7],7))
