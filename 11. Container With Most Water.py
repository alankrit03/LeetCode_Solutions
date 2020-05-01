class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0

        i, j = 0, len(height) - 1

        ans = 0

        while j - i > 0:
            ans = max(ans, (j - i) * min(height[i], height[j]))

            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return ans