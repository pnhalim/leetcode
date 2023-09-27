class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = datetime.date(year=int(date1[0:4]), month=int(date1[5:7]), day=int(date1[8:10]))
        d2 = datetime.date(year=int(date2[0:4]), month=int(date2[5:7]), day=int(date2[8:10]))
        if d1 == d2:
            return 0
        return int(abs(d2 - d1).days)