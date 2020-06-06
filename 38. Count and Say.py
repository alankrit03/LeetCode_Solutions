class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        elif n == 2:
            return '11'
        elif n == 3:
            return '21'
        prev = self.countAndSay(n - 1)

        count = 0
        curr = prev[0]
        ans = ''

        for x in prev:
            if x == curr:
                count += 1
            else:
                ans += str(count) + curr
                curr = x
                count = 1
        ans += str(count) + curr
        return ans