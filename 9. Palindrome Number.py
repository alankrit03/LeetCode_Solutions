class Solution:
    def isPalindrome(self, x: int):
        if x < 0:
            return False
        new_n = 0
        n = x
        while x:
            d = x % 10
            new_n = new_n * 10 + d
            x = x // 10

        # print(n , new_n)
        if n == new_n:
            return True
        else:
            return False