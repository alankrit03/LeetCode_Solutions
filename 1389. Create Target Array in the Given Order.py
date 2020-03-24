class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []

        for x, y in zip(index, nums):
            target.insert(x, y)

        return target