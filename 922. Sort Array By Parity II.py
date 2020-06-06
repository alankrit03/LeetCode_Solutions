class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        n = len(A)

        def misplaced_odd(idx):
            for i in range(idx, n):
                if not i % 2 and A[i] % 2:
                    return i

        def misplaced_even(idx):
            for i in range(idx, n):
                if i % 2 and not A[i] % 2:
                    return i

        for i in range(n):
            if i % 2 and not A[i] % 2:
                temp = misplaced_odd(i + 1)
                A[i], A[temp] = A[temp], A[i]

            if not i % 2 and A[i] % 2:
                temp = misplaced_even(i + 1)
                A[i], A[temp] = A[temp], A[i]

        return A