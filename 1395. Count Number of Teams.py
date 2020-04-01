import sys

sys.setrecursionlimit(10000000)


class Solution:
    def __init__(self):
        self.answer = 0

    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)

        def countincreasing(val, i, count):
            if count == 3:
                self.answer += 1
                return

            if i == n:
                return

            for j in range(i, n):
                if rating[j] > val:
                    countincreasing(rating[j], j + 1, count + 1)

        def countdecreasing(val, i, count):
            if count == 3:
                self.answer += 1
                return

            if i == n:
                return

            for j in range(i, n):
                if rating[j] < val:
                    countdecreasing(rating[j], j + 1, count + 1)

        for i in range(n):
            countincreasing(rating[i], i + 1, 1)
            countdecreasing(rating[i], i + 1, 1)

        return self.answer