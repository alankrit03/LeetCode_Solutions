class Solution:
    def removeDuplicates(self, S: str) -> str:
        hasChanged = True

        n = len(S)
        size = n
        while hasChanged:
            hasChanged = False
            i = 0
            temp = ''
            while i < n:
                if i < n - 1 and S[i] == S[i + 1]:
                    hasChanged = True
                    i += 1
                    size -= 2
                else:
                    temp += S[i]
                i += 1
            S = temp
            n = size
        return S


ob = Solution()
print(ob.removeDuplicates('abbaca'))