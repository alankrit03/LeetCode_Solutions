class Solution:
    def binaryGap(self, n: int) -> int:
        k = bin(n)[2:]
        ans = 0
        prev = None

        for i in range(len(k)):
            if k[i] == '1':
                try:
                    ans = max(ans, i - prev)
                    prev = i
                except:
                    prev = i

        # print(k)
        return ans