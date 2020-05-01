class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        temp = c.most_common(k)
        ans = []

        for x, _ in temp:
            ans.append(x)

        return ans