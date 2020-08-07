class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        employee = collections.defaultdict(list)

        for i in range(n):
            if manager[i] > -1:
                employee[manager[i]].append(i)

        def recur(boss):
            try:
                subs = employee[boss]
            except:
                return 0

            time = 0
            for sub in subs:
                time = max(time, recur(sub))

            return time + informTime[boss]

        return recur(headID)