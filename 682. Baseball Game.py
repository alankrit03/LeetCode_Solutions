class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []

        sum_ = 0

        for x in ops:
            if x == 'C':
                sum_ -= stack.pop()
            elif x == 'D':
                sum_ += 2 * stack[-1]
                stack.append(2 * stack[-1])
            elif x == '+':
                sum_ += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            else:
                sum_ += int(x)
                stack.append(int(x))

        return sum_