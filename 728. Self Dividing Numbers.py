class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isTrue(n):
            temp = n
            while temp:
                d = temp % 10
                if d and n % d == 0:
                    temp //= 10
                else:
                    return False
            return True

        ans = []

        for i in range(left, right + 1):
            if isTrue(i):
                ans.append(i)

        return ans