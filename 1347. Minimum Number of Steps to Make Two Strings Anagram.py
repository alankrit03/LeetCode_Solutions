class Solution:
    def minSteps(self, s: str, t: str) -> int:
        t = collections.Counter(t)
        for x in s:
            if t.get(x,0)>0:
                t[x]-=1
        # print(t.values())
        return sum(t.values())