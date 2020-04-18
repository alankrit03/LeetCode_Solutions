class Solution:
    def reverse(self, x: int) -> int:
        temp = str(x)
        if x >= 0:
            ans = int(temp[::-1])
        else:
            temp = temp[1:]
            ans = int('-' + temp[::-1])

        if ans < -2 ** 31 or ans >= 2 ** 31:
            return 0
        return ans