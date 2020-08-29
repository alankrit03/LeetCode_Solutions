import string


class Solution:
    def titleToNumber(self, s: str) -> int:
        letters = string.ascii_uppercase
        cache = dict(zip(letters, range(1, 27)))
        # print(cache)

        ans = 0
        power = 0
        for x in s[::-1]:
            ans += cache[x] * (26 ** power)
            power += 1

        return ans