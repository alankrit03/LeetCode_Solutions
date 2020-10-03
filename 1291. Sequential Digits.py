class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def build(l, f):
            num = f
            l -= 1
            while l:
                f += 1
                num = num * 10 + f
                l -= 1
            return num

        l = len(str(low))
        h = len(str(high))
        ans = []
        for i in range(l, h + 1):
            for j in range(1, 11 - i):
                num = build(i, j)
                # print(num)
                if low <= num <= high:
                    ans.append(num)

        return ans