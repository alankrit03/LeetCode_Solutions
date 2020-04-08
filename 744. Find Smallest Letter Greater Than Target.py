class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        if not n:
            return
        l, h = 0, n

        while h - l > 1:
            m = (h + l) // 2

            if letters[m] > target:
                h = m
            else:
                l = m
        if l == 0 and letters[0] > target:
            return letters[0]
        return letters[(l + 1) % n]