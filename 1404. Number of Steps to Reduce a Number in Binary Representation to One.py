from collections import deque
class Solution:
    def numSteps(self, s: str) -> int:
        s = deque(s[::-1])
        count = 0
        n = len(s)
        while n>1:
            if s[0]=='1':
                count += 1
                i=0
                while i<n :
                    if s[i]=='0':
                        s[i]='1'
                        break
                    else:
                        s[i]='0'
                    i+=1
                else:
                    n+=1
                    s.append('1')
            else:
                s.popleft()
                count +=1
                n-=1
        return count