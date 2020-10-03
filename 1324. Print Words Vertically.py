class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        max_ = -1

        for i in range(len(s) - 1, -1, -1):
            curr = len(s[i])
            max_ = max(curr, max_)

            s[i] += ' ' * (max_ - curr)

        ans = []
        for i in range(max_):
            t = ''
            for x in s:
                try:
                    t += x[i]
                except:
                    break
            ans.append(t)

        return ans