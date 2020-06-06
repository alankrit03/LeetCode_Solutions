class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_list = list(enumerate(arr))
        sorted_list.sort(key=lambda x: x[1])
        if not arr:
            return
        rank = 1
        curr = sorted_list[0][1]

        for x in sorted_list:
            if curr != x[1]:
                rank += 1
                curr = x[1]

            arr[x[0]] = rank
        return arr