import collections


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = collections.Counter(nums)
        return (a.most_common()[0][0])
