class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if not A:
            return

        i = j = 0

        while j < len(A):
            if i!=j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j += 1
            while j < len(A) and A[j] % 2:
                j += 1

        return A