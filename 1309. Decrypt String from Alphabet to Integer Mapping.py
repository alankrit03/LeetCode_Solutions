class Solution:
    def freqAlphabets(self, s: str) -> str:
        ele = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
        key = ['1', '2', '3', '4', '5',
               '6', '7', '8', '9', '10#',
               '11#', '12#', '13#', '14#',
               '15#', '16#', '17#', '18#',
               '19#', '20#', '21#', '22#', '23#', '24#', '25#', '26#'
               ]
        cache = {x: y for x, y in zip(key, ele)}

        n = len(s)
        ans = ''
        i = 0
        while i < n:
            if i + 2 < n and s[i + 2] == '#':
                ans += cache[s[i:i + 3]]
                i += 3
            else:
                ans += cache[s[i]]
                i += 1

        return ans