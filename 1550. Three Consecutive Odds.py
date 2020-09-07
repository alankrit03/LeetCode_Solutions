class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        flag = 3
        for x in arr:
            if x % 2:
                if flag == 1:
                    return True
                flag -= 1
            else:
                flag = 3

        return False