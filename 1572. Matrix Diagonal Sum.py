class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        side = len(mat)
        ans = 0

        for i in range(side):
            ans += mat[i][i]
            ans += mat[i][side - i - 1]

        if side % 2:
            ans -= mat[side // 2][side // 2]

        return ans