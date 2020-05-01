class Solution:
    from collections import Counter
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)

        c = c.most_common()
        c.sort(key=lambda x: (-x[1], x[0]))

        ans = []
        for x, _ in c:
            ans.append(x)

        return ans[:k]