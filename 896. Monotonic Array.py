class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        n = len(A)

        if n == 1:
            return True

        isIncreasing = True if A[-1] - A[0] >= 0 else False

        for i in range(1, n):
            if A[i] - A[i - 1] == 0:
                continue
            if ((A[i] - A[i - 1] > 0) ^ isIncreasing):
                return False

        return True