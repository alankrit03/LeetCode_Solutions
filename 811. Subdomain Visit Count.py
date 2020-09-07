class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cache = {}

        for d in cpdomains:
            c, d = d.split()
            c = int(c)
            s = ''
            for i in range(len(d) - 1, -1, -1):
                if d[i] == '.':
                    if s in cache:
                        cache[s] += c
                    else:
                        cache[s] = c
                s = d[i] + s
            else:
                if s in cache:
                    cache[s] += c
                else:
                    cache[s] = c

        ans = []
        for key, val in cache.items():
            ans.append(str(val) + " " + key)

        return ans