class Solution:
    def convertToTitle(self, n: int) -> str:
        letters = string.ascii_uppercase

        s = ''
        while n:
            d = n % 26
            s = letters[d - 1] + s
            # print(d,n)
            if not d:
                n = n - 1
            n //= 26

        return s