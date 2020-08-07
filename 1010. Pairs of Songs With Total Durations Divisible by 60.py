class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        check = [0] * 60

        for x in time:
            check[x % 60] += 1

        count = 0
        for i in [0, 30]:
            count += ((check[i] - 1) * check[i]) // 2

        for i in range(1, 30):
            count += check[i] * check[60 - i]

        return count