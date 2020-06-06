from collections import Counter


class Solution:
    def commonChars(self, A: list[str]):
        ans = Counter(A[0])

        for i in range(1, len(A)):
            temp = ans - Counter(A[i])
            ans -= temp

        return list(ans.elements())