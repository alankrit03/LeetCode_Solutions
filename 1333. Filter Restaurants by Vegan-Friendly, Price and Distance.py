class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], vegan: int, maxPrice: int, maxDistance: int) -> List[int]:
        ans = []
        n = 0
        for each in restaurants:
            if each[2] >= vegan and each[3] <= maxPrice and each[4] <= maxDistance:
                ans.append([each[0], each[1]])
                n += 1

        def sortFn(x):
            return (-x[1], -x[0])

        ans.sort(key=sortFn)
        for i in range(n):
            ans[i] = ans[i][0]
        return ans