import math
import string


class Solution:
    def __init__(self):
        self.__cache = {}
        for x, y in enumerate(list(string.ascii_lowercase)):
            self.__cache[y] = x + 1

    def repeatedStringMatch(self, A: str, B: str) -> int:
        def find_substring(st, pat):
            def cal_weight(s: str):
                n = len(s)
                total = 0
                for x in s:
                    total += self.__cache[x] * (26 ** n)
                    n -= 1
                return total

            def roll_hash(value, prv, nxt):
                value -= self.__cache[st[prv]] * (26 ** m)
                value *= 26
                value += self.__cache[st[nxt]] * 26
                return value

            n = len(st)
            m = len(pat)

            value = cal_weight(pat)
            curr = cal_weight(st[:m])

            if value == curr and pat == st[:m]:
                return True

            i = 0
            j = m

            while j < n:
                curr = roll_hash(curr, i, j)
                i += 1
                j += 1
                if curr == value and pat == st[i:j]:
                    return True
            return False

        if not set(B).issubset(set(A)):
            return -1

        a = len(A)
        b = len(B)
        n = math.ceil(b / a)

        if find_substring(A * n, B):
            return n
        elif find_substring(A * (n + 1), B):
            return n + 1
        return -1
