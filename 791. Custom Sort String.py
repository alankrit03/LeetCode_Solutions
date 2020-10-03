import collections


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        c = collections.Counter(T)

        T = ''
        for x in S:
            if x in c:
                T += x * c[x]
                del c[x]
        else:
            for x in c.keys():
                T += x * c[x]

        return T