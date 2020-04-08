class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, h = 0, num

        while l <= h:
            m = (h + l) // 2

            if m ** 2 == num:
                return True
            elif m ** 2 > num:
                h = m - 1
            else:
                l = m + 1
        return False
