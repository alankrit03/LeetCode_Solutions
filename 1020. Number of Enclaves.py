class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        row = len(A)
        col = len(A[0])

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        def dfs(i, j):
            if i < 0 or j < 0 or i >= row or j >= col:
                return None

            if not A[i][j]:
                return 0

            A[i][j] = 0
            ans = 0
            touching = False
            for d in range(4):
                try:
                    ans += dfs(i + dr[d], j + dc[d])
                except:
                    touching = True
            if touching:
                return None
            return ans + 1

        ans = 0
        for i in range(row):
            for j in range(col):
                if A[i][j]:
                    # print(i,j)
                    try:
                        ans += dfs(i, j)
                    except:
                        pass
                    # print(ans)
        return ans