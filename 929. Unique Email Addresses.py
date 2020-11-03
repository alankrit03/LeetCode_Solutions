class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        cache = set()
        ans = 0
        for x in emails:
            temp = ''
            for i in range(len(x)):
                y = x[i]
                if y == '@':
                    temp += x[i:]
                    if temp not in cache:
                        ans += 1
                        cache.add(temp)
                    break
                elif y == '+':
                    pos = x.index('@')
                    temp += x[pos:]
                    if temp not in cache:
                        ans += 1
                        cache.add(temp)
                    break
                elif y != '.':
                    temp += y

        return ans