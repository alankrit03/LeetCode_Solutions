import calendar
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        c = calendar.weekday(year,month,day)
        return calendar.day_name[c]