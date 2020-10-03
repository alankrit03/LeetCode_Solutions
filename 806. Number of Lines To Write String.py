class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        dic = {}
        i = 0
        for x in string.ascii_lowercase:
            dic[x] = i
            i += 1

        ans = [1, 0]
        for x in S:
            n = widths[dic[x]]
            if ans[1] + n > 100:
                ans[0] += 1
                ans[1] = n
            else:
                ans[1] += n

        return ans