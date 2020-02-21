class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        last_row = self.getRow(rowIndex - 1)

        ans = [1] + [last_row[i] + last_row[i + 1] for i in range(rowIndex - 1)] + [1]

        return ans