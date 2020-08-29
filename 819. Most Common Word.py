import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        banned = set(banned)
        words = re.findall('[a-z]+',paragraph)
        # print(words)
        c = collections.Counter(words)
        c = c.most_common()
        for x,_ in c:
            if x not in banned:
                return x
        return 'ball'