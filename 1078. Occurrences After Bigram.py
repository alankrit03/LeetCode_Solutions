class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        n = len(text)

        ans = []

        for i in range(n):
            x = text[i]
            if x == first:
                try:
                    if text[i + 1] == second:
                        try:
                            ans.append(text[i + 2])
                        except:
                            pass
                except:
                    pass
        return ans