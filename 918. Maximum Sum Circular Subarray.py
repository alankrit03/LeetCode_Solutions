class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if not A:
            return 0
        n = len(A)

        ans = cur = 0
        for x in A:
            cur = x + max(cur, 0)
            ans = max(ans, cur)

        rightsum = [0] * n
        rightsum[-1] = A[-1]
        for i in range(n - 2, -1, -1):
            rightsum[i] = rightsum[i + 1] + A[i]

        maxright = [0] * n
        maxright[-1] = rightsum[-1]
        for i in range(n - 2, -1, -1):
            maxright[i] = max(maxright[i + 1], rightsum[i])

        leftsum = 0
        for i in range(n - 2):
            leftsum += A[i]
            ans = max(ans, leftsum + maxright[i + 2])
        if ans == 0:
            return max(A)
        return ans