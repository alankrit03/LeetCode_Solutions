class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        self.ans = []
        n = len(S)

        def recur(idx, temp):
            if idx == n:
                self.ans.append(''.join(temp))
                return

            x = S[idx]
            if x.isalpha():
                x = x.lower()
                temp.append(x)
                recur(idx + 1, temp)
                temp.pop()
                x = x.upper()
                temp.append(x)
                recur(idx + 1, temp)
                temp.pop()
                return
            else:
                temp.append(x)
                recur(idx + 1, temp)
                temp.pop()

        recur(0, [])
        return self.ans