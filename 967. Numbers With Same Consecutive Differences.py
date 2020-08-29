class Solution:
    def numsSameConsecDiff(self, N: int, k: int) -> List[int]:
        self.ans = []
        if N == 1:
            self.ans.append(0)
        if not k:
            for i in range(1, 10):
                self.ans.append(int(str(i) * N))
            return self.ans

        def recur(x, digits):
            if digits == N:
                self.ans.append(x)
                return
            d = x % 10
            if d - k > -1:
                recur(x * 10 + (d - k), digits + 1)
            if d + k < 10:
                recur(x * 10 + (d + k), digits + 1)

        for i in range(1, 10):
            recur(i, 1)

        return self.ans