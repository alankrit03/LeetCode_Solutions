class Solution:
    import sys
    sys.setrecursionlimit(100000)

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        if not s: return s

        x = s.pop(0)
        self.reverseString(s)
        s.append(x)

