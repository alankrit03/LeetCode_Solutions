class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i=0
        j = len(s)-1
        cache = set('aeiouAEIOU')
        while i<j:
            if s[i] in cache and s[j] in cache:
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
            elif s[i] in cache:
                j-=1
            elif s[j] in cache:
                i+=1
            else:
                i+=1
                j-=1
        return ''.join(s)