class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        ans = []

        for i in range(m):
            ele = min(matrix[i])
            pos = matrix[i].index(ele)
            for j in range(m):
                if matrix[j][pos] > ele:
                    break
            else:
                ans.append(ele)

        return ans