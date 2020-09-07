class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        cache1 = {}
        cache2 = {}
        n1 = len(pattern)
        n2 = len(s)
        if n1!=n2:
            return False
        for i in range(n1):
            key = pattern[i]
            val = s[i]
            # print(key,val)
            if key in cache1:
                if cache1[key]!=val:
                    return False
            elif val in cache2:
                if cache2[val]!= key:
                    return False
            else:
                cache1[key]=val
                cache2[val]=key
        return True