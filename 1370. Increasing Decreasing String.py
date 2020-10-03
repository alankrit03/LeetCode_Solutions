class Solution:
    def sortString(self, s: str) -> str:
        data = collections.Counter(s)
        arr = list(data.keys())
        arr.sort()
        hasChanged = False
        s = ''
        while 1:
            for x in arr:
                if data[x]:
                    s += x
                    data[x] -= 1
                    hasChanged = True
            if hasChanged:
                hasChanged = False
            else:
                break

            for x in arr[::-1]:
                if data[x]:
                    s += x
                    data[x] -= 1
                    hasChanged = True
            if hasChanged:
                hasChanged = False
            else:
                break
        return s
