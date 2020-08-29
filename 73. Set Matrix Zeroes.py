class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def putA(i, j):
            for x in range(m):
                if matrix[i][x]:
                    matrix[i][x] = 'A'
            for y in range(n):
                if matrix[y][j]:
                    matrix[y][j] = 'A'

        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    putA(i, j)

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 'A':
                    matrix[i][j] = 0
