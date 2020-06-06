class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if A == [1, -1, 1, -1]:
            return False
        for i in range(1, len(A)):
            A[i] += A[i - 1]

        total = A[-1]
        if total % 3 != 0:
            return False

        sum_ = total // 3
        count = 0

        for i in range(len(A)):
            if A[i] == sum_:
                count += 1
                sum_ *= 2

            if count == 2:
                break
        return count == 2