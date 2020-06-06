class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_height = sorted(heights)
        ans = 0

        for i in range(len(heights)):
            if heights[i] != sorted_height[i]:
                ans += 1

        return ans