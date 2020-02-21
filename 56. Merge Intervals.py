"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""


def merge(intervals):
    res = [intervals[0]]

    for i in range(1, n):
        if intervals[i][0] <= res[-1][1]:
            if intervals[i][1] > res[-1][1]:
                res[-1][1] = intervals[i][1]
        else:
            res.append(intervals[i])

    return res


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
n = len(intervals)
ans = merge(intervals)
print(ans)
