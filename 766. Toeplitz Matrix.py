class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        prev = matrix[0]

        for i in range(1, len(matrix)):
            curr = matrix[i]
            if prev[:-1] != curr[1:]:
                return False
            prev = curr

        return True