class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        isPossible = True
        n = len(A)
        ans = []

        for k in range(1, 7):
            isPossible = True
            a = 0
            b = 0
            for i in range(n):
                if A[i] != k and B[i] != k:
                    isPossible = False
                    break
                elif A[i] == B[i]:
                    continue
                elif A[i] == k:
                    a += 1
                else:
                    b += 1
            if isPossible:
                ans.append(min(a, b))
            else:
                ans.append(n)

        if min(ans) == n:
            return -1
        return min(ans)