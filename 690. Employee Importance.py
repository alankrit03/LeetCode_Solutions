"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], idn: int) -> int:
        self.total = 0
        employee_dict = {}

        for emp in employees:
            employee_dict[emp.id] = emp

        def DFS(x):
            emp = employee_dict[x]
            self.total += emp.importance

            for x in emp.subordinates:
                DFS(x)

        DFS(idn)
        return self.total