class Solution:
    def numSpecial(self, mat) -> int:
        row = len(mat)
        if not row:
            return 0
        col = len(mat[0])
        if not col:
            return 0

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        def DFS(i, j, d):
            if i < 0 or j < 0 or i >= row or j >= col:
                return True

            if mat[i][j]:
                mat[i][j] = 2
                return False

            return DFS(i + dr[d], j + dc[d], d)

        ans = 0
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1:
                    print(i, j)
                    temp = True
                    for d in range(4):
                        temp = temp and DFS(i + dr[d], j + dc[d], d)
                        print(temp)
                    if temp:
                        ans += 1

        return ans

ob = Solution()
mat = [[1,0,0],[0,0,1],[1,0,0]]
print(ob.numSpecial(mat))