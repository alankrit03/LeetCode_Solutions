class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        cache = {}
        for i in range(len(list1)):
            cache[list1[i]] = i

        ans = []
        min_ = len(list1) + len(list2)

        for i in range(len(list2)):
            if list2[i] in cache:
                ans.append((list2[i], i + cache[list2[i]]))

                min_ = min(min_, i + cache[list2[i]])

        i = 0
        while i < len(ans):
            if ans[i][1] == min_:
                ans[i] = ans[i][0]
                i += 1
            else:
                del ans[i]

        return ans