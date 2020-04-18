class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        def show_brackets(st, left, right):
            if left + right == 2 * n:
                self.ans.append(st)
                return 0

            if left == right:
                show_brackets(st + '(', left + 1, right)

            else:
                if left == n:
                    show_brackets(st + ')', left, right + 1)
                else:
                    show_brackets(st + '(', left + 1, right)
                    show_brackets(st + ')', left, right + 1)


        str1 = ''
        show_brackets(str1, 0, 0)
        return self.ans
