class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        letters = string.ascii_lowercase
        dic = {x: y for y, x in enumerate(letters)}
        # print(dic)

        n = len(shifts)
        for i in range(n - 2, -1, -1):
            shifts[i] += shifts[i + 1]

        new_s = [''] * n
        for i in range(n):
            e = s[i]
            e = (dic[e] + 1 + shifts[i]) % 26
            new_s[i] = letters[e - 1]
        return ''.join(new_s)