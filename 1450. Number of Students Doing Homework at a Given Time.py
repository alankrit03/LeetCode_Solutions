class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        students = 0

        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                students += 1

        return students