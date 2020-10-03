class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        n = len(S)
        i, j = 0, n - 1
        S = list(S)
        cache = set(string.ascii_lowercase + string.ascii_uppercase)

        while i < j:
            while i < n and S[i] not in cache:
                i += 1
            while j >= 0 and S[j] not in cache:
                j -= 1

            if i < j:
                S[i], S[j] = S[j], S[i]
                i += 1
                j -= 1

        return ''.join(S)