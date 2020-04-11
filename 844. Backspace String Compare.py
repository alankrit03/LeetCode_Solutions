class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = []
        t = []

        for i in range(len(S)):
            if S[i] == '#':
                if len(s):
                    s.pop()
            else:
                s.append(S[i])

        for i in range(len(T)):
            if T[i] == '#':
                if len(t):
                    t.pop()
            else:
                t.append(T[i])

        if s == t:
            return True