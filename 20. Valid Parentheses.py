class Solution:
    def isValid(self, s: str) -> bool:
        cache = {')': '(', '}': '{', ']': '['}

        stack = []

        for i in range(len(s)):
            if s[i] in cache:
                if not stack or stack[-1] != cache[s[i]]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(s[i])

        return not stack