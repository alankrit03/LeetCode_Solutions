class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        flag = 3
        ans = ''
        for x in n[::-1]:
            if not flag:
                ans = '.'+ans
                flag = 3
            ans = x+ans
            flag -=1
        return ans