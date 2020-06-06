from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = Counter(chars)

        ans = 0

        for word in words:
            if not bool(Counter(word) - chars):
                ans += len(word)

        return ans