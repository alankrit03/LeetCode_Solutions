class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        row = len(A)
        col = len(A[0])
        if row == col:
            for i in range(1, len(A)):
                for j in range(i):
                    A[i][j], A[j][i] = A[j][i], A[i][j]
            return A
        else:
            B = []
            for i in range(col):
                temp = []
                for j in range(row):
                    temp.append(A[j][i])

                B.append(temp)

        return B