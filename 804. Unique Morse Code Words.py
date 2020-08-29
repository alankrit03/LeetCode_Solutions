class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        temp = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        morse = {x: y for x, y in zip(string.ascii_lowercase, temp)}

        # print(morse)
        n = 0
        cache = set()
        for word in words:
            st = ''
            for l in word:
                st += morse[l]
            if st not in cache:
                cache.add(st)
                n += 1
        return n