class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        if numRows == 1:
            return [[1]]

        ans = [[1], [1, 1]]

        for i in range(3, numRows + 1):
            temp1 = ans[-1]
            temp = [1] + [temp1[i] + temp1[i + 1] for i in range(len(temp1) - 1)] + [1]
            ans.append(temp)

        return ans
