class Solution:
    from collections import Counter
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter()

        for x in arr2:
            c[x] = 0

        left_list = []

        for x in arr1:
            if x in c:
                c[x] += 1
            else:
                left_list.append(x)

        left_list.sort()

        left_list = list(c.elements()) + left_list

        return left_list