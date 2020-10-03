class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        total_1 = 0
        total_2 = 0

        for x in s:
            total_1 += ord(x)

        for x in t:
            total_2 += ord(x)

        return chr(total_2 - total_1)


"""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Approach 2:

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t = collections.Counter(t)
        for x in s:
            t[x] -= 1

        return t.most_common(1)[0][0]