class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return
        cur = a ** b[0] % 1337
        for i in range(1, len(b)):
            cur = cur ** 10 * a ** b[i] % 1337
        return cur % 1337