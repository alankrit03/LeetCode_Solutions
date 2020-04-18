class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans = [0] * len(A)
        i, j = 0, len(A) - 1
        idx = j
        while i <= j:
            if abs(A[i]) > abs(A[j]):
                ans[idx] = A[i] ** 2
                i += 1
            else:
                ans[idx] = A[j] ** 2
                j -= 1
            idx -= 1

        return ans