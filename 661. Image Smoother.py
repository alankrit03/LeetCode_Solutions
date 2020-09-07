class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        row = len(M)
        col = len(M[0])

        dr = [-1, -1, 0, 1, 1, 1, 0, -1]
        dc = [0, 1, 1, 1, 0, -1, -1, -1]

        def get_value(i, j):
            if i < 0 or j < 0 or i >= row or j >= col:
                return None
            return M[i][j]

        dp = [[0] * col for i in range(row)]

        for i in range(row):
            for j in range(col):
                sum_ = 0
                ele = 0

                for d in range(8):
                    try:
                        sum_ += get_value(i + dr[d], j + dc[d])
                        ele += 1
                    except:
                        pass
                sum_ += M[i][j]
                ele += 1
                dp[i][j] = sum_ // ele

        return dp
