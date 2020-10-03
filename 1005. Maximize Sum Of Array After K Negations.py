class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        ans = sum(A)
        A.sort()

        for i in range(len(A)):
            if not K or A[i] == 0:
                break
            if A[i] < 0:
                ans -= 2 * A[i]
                K -= 1
            else:
                if K % 2:
                    if i and A[i] > abs(A[i - 1]):
                        ans += 2 * A[i - 1]
                    else:
                        ans -= 2 * A[i]
                break

        return ans