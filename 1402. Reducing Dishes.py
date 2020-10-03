class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        ans = total = sum_ = 0

        satisfaction.sort(reverse=True)

        for x in satisfaction:
            sum_ += x
            total += sum_
            ans = max(ans, total)

        return ans
