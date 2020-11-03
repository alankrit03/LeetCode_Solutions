class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastIdx = {ch: i for i, ch in enumerate(s)}
        stack = []
        cache = set()

        for i, ch in enumerate(s):
            if ch in cache:
                continue
            while stack and ch < stack[-1] and lastIdx[stack[-1]] > i:
                cache.remove(stack.pop())

            cache.add(ch)
            stack.append(ch)
        return ''.join(stack)