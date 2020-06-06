class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def getStrength(i):
            l, h = -1, col

            while h - l > 1:
                m = (l + h) // 2
                if mat[i][m]:
                    l = m
                else:
                    h = m
            return l + 1

        strength = [[i, 0] for i in range(len(mat))]

        row = len(mat)
        col = len(mat[0])

        for i in range(row):
            strength[i][1] = getStrength(i)

        strength.sort(key=lambda x: x[1])
        result = []
        for i in range(k):
            result.append(strength[i][0])
        return result