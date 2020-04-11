class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return

        ans = []
        m = len(matrix)
        n = len(matrix[0])

        for x in range(n):
            temp = []
            i = 0
            j = x
            while j >= 0 and i < m:
                temp.append(matrix[i][j])
                j -= 1
                i += 1

            if x % 2 == 0:
                temp.reverse()
            ans.extend(temp)

        for x in range(1, m):
            temp = []
            j = n - 1
            i = x
            while i < m and j >= 0:
                temp.append(matrix[i][j])
                i += 1
                j -= 1
            if (x + n - 1) % 2 == 0:
                temp.reverse()
            ans.extend(temp)

        return ans
