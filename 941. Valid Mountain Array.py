class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        increasing = True
        if len(A) < 3 or A[1] <= A[0]:
            return False

        for i in range(1, len(A)):
            if A[i] == A[i - 1]:
                return False

            if increasing and A[i] < A[i - 1]:
                increasing = False

            if not increasing and A[i] > A[i - 1]:
                return False

        if increasing:
            return False
        return True