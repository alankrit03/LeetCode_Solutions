class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        i = 0
        j = len(S)
        ans = [0]*(j+1)
        for idx in range(len(S)):
            if S[idx]=='I':
                ans[idx] = i
                i+=1
            else:
                ans[idx] = j
                j-=1
        ans[idx+1] = i
        return ans