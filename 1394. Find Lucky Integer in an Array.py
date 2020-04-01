class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mydic = {}
        for x in arr:
            if mydic.get(x):
                mydic[x] += 1
            else:
                mydic[x] = 1
        ans = -1

        for key, value in mydic.items():
            if key == value and key > ans:
                ans = key

        return ans