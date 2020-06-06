class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        odd_num = 0
        even_num = 0

        for x in chips:
            if x % 2:
                odd_num += 1
            else:
                even_num += 1

        return min(odd_num, even_num)